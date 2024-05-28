import numpy as np
import plotly.express as px
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

import planodeleituraanual.database as db


def index(tab: DeltaGenerator):

    row = tab.columns([1.2, 0.8])

    row[0].write('## Leitura')

    data = row[0].date_input('Data Específica:', format='DD/MM/YYYY')

    leituras = db.get_bread_daily(data)
    if not leituras:
        if data.strftime('%m-%d') == '02-29':
            row[0].error('Esse ano é bissexto, o dia 29/02 não está no plano.')
        else:
            row[0].error('Ops! Algo deu errado!')
    else:
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

    options = ['Por Livro', 'Por Capítulo']

    selected = row[1].selectbox('Acompanhar Por:', options)

    if selected == options[0]:
        livro = (
            st.session_state.biblia_df.groupby('status')['capitulos']
            .count()
            .reset_index()
        )
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
        capitulos = st.session_state.biblia_df.sum()
        fig = px.pie(
            capitulos,
            values=[capitulos['capitulos'], capitulos['capitulos_lidos']],
            names=['Não Lido', 'Lido'],
            title='Total de Capítulos Lidos',
        )
        row[1].plotly_chart(fig, True)
