import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

if __name__ == '__main__':

    st.set_page_config('Plano de Leitura Anual', ':book:', 'wide')

    st.write('# Plano de Leitura Anual')
    st.divider()

    df = pd.read_excel('biblia.ods', engine='odf')

    df = df.drop(['pagina_inicial'], axis=1)

    df['lido'] = [True if i == 1 else False for i in df['lido']]

    row = st.columns(3)

    livro = df.groupby('lido')['livro'].count().reset_index()
    livro['lido'] = np.where(livro['lido'], 'Lido', 'Não lido')

    fig = px.pie(
        livro, values='livro', names='lido', title='Percentual lido por livros'
    )

    row[0].plotly_chart(fig, True)

    qtd_paginas = df.groupby('lido')['quantidade_paginas'].sum().reset_index()
    qtd_paginas['lido'] = np.where(qtd_paginas['lido'], 'Lido', 'Não lido')

    fig = px.pie(
        qtd_paginas,
        values='quantidade_paginas',
        names='lido',
        title='Percentual lido por páginas',
    )

    row[1].plotly_chart(fig, True)

    capitulos = df.groupby('lido')['capitulos'].sum().reset_index()
    capitulos['lido'] = np.where(capitulos['lido'], 'Lido', 'Não lido')

    fig = px.pie(
        capitulos,
        values='capitulos',
        names='lido',
        title='Percentual lido por capítulos',
    )

    row[2].plotly_chart(fig, True)
