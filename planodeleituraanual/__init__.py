import numpy as np
import plotly.express as px
import streamlit as st
from dotenv import dotenv_values

import planodeleituraanual.database as db
from planodeleituraanual.create_plan import create_plan
from planodeleituraanual.functions import load_biblia_df
from planodeleituraanual.shutdown import btn_shutdown, shutdown


def create_app():

    config = dotenv_values('.env')

    if db.get_usuario() is None:
        create_plan()
    else:
        st.set_page_config(config['APP_NAME'], ':book:', 'wide')

        shutdown()

        st.write('# {}'.format(config['APP_NAME']))

        container = st.container()

        row = container.columns([1.2, 0.8])

        row[0].write('## Leitura')

        data = row[0].date_input('Data Específica:', format='DD/MM/YYYY')

        leituras = db.get_bread_daily(data)

        row[0].divider()

        for item in leituras:
            row_leituras = row[0].columns([1.5, 0.5])
            row_leituras[0].write('##### {}'.format(item.replace('_', ' ')))
            row_leituras[1].toggle(
                'Marque como Lido',
                value=db.is_chapter_read(item),
                key=item,
                on_change=db.set_chapter_read,
                args=[item],
            )

        row[1].write('## Progresso')

        df = load_biblia_df()

        df['capitulos_lidos'] = [
            db.count_chapters_read(x) for x in df['livro']
        ]

        df['status'] = np.where(
            df['capitulos'] == df['capitulos_lidos'], True, False
        )

        options = ['Por Livro', 'Por Capítulo']

        selected = row[1].selectbox('Acompanhar Por:', options)

        if selected == options[0]:
            livro = df.groupby('status')['capitulos'].count().reset_index()
            livro['status'] = np.where(
                livro['status'] == False, 'Não concluído', 'Concluído'
            )
            fig = px.pie(
                livro,
                values='capitulos',
                names='status',
                title='Total de Livros Lidos',
            )
            row[1].plotly_chart(fig, True)

        if selected == options[1]:
            capitulos = df.sum()
            fig = px.pie(
                capitulos,
                values=[capitulos['capitulos'], capitulos['capitulos_lidos']],
                names=['Não Lido', 'Lido'],
                title='Total de Capítulos Lidos',
            )
            row[1].plotly_chart(fig, True)

    btn_shutdown()
