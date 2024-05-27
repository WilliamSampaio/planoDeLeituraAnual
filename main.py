import json

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

if __name__ == '__main__':

    st.set_page_config('Plano de Leitura Anual', ':book:', 'wide')

    st.write('# Plano de Leitura Anual')
    st.divider()

    df = pd.read_excel('biblia.ods', engine='odf')
    df = df.drop(['pagina_inicial', 'quantidade_paginas'], axis=1)
    df['status'] = np.where(
        df['capitulos'] == df['capitulos_lidos'], 'Lidos', 'Não Lidos'
    )

    df['contador'] = 0

    f = open('plano.json')
    plano = json.load(f)

    for dia in plano:
        for leitura in plano[dia]:
            livro_cap = str(leitura).split('_')
            for i in range(0, len(df['livro'])):
                if df['livro'][i] == livro_cap[0]:
                    df['contador'][i] = df['contador'][i] + 1

    df['ok'] = np.where(df['capitulos'] == df['contador'], 'OK', '---')

    df = st.data_editor(df, width=2000)

    row = st.columns(2)

    options = ['Por livro', 'Por capítulo']

    selected = row[1].selectbox('Progresso', options)

    if selected == options[0]:
        livro = df.groupby('status')['livro'].count().reset_index()
        fig = px.pie(
            livro,
            values='livro',
            names='status',
            title='Percentual lido por livros',
        )
        row[1].plotly_chart(fig, True)

    if selected == options[1]:
        capitulos = df.sum()
        fig = px.pie(
            capitulos,
            values=[capitulos['capitulos'], capitulos['capitulos_lidos']],
            names=['Não Lidos', 'Lidos'],
            title='Percentual lido por capítulos',
        )
        row[1].plotly_chart(fig, True)

    # st.latex('TESTE')
    # st.divider()

    # st.toast('teste')

    # tab = st.tabs(['# teste', '# teste'])

    # # st.snow()

    # st.header('teste')
    # st.subheader('teste')

    # # st.switch_page()

    # tab[0].error('teste 1')
    # tab[1].error('teste 2')

    # qtd_paginas = df.groupby('lido')['quantidade_paginas'].sum().reset_index()
    # qtd_paginas['lido'] = np.where(qtd_paginas['lido'], 'Lido', 'Não lido')

    # fig = px.pie(
    #     qtd_paginas,
    #     values='quantidade_paginas',
    #     names='lido',
    #     title='Percentual lido por páginas',
    # )

    # row[1].plotly_chart(fig, True)

    # st.dataframe(capitulos)
