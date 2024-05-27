import numpy as np
import pandas as pd
import streamlit as st
from dotenv import dotenv_values

import database as db
from create_plan import create_plan


if __name__ == '__main__':

    if db.get_usuario() is None:
        create_plan()
    else:

        config = dotenv_values('.env')

        st.set_page_config(config['APP_NAME'], ':book:', 'wide')

        st.write('# {}'.format(config['APP_NAME']))
        st.divider()

        container = st.container()

        row = container.columns(2)

        row[0].write('## Leitura')

        data = row[0].date_input('Data Específica:')

        leituras = db.get_bread_daily(data)['leituras']

        st.write(leituras)

        df = pd.read_excel('biblia.ods', engine='odf')
        df = df.drop(['pagina_inicial', 'quantidade_paginas'], axis=1)
        df['status'] = np.where(
            df['capitulos'] == df['capitulos_lidos'], 'Lidos', 'Não Lidos'
        )

        # st.write(tbl.get(doc_id=99))

        # df['contador'] = 0

        # f = open('plano.json')
        # plano = json.load(f)

        # for dia in plano:
        #     for leitura in plano[dia]:
        #         livro_cap = str(leitura).split('_')
        #         for i in range(0, len(df['livro'])):
        #             if df['livro'][i] == livro_cap[0]:
        #                 df['contador'][i] = df['contador'][i] + 1

        # df['ok'] = np.where(df['capitulos'] == df['contador'], 'OK', '---')

        # df = st.data_editor(df, width=2000)
        ##################################################################
        # row = st.columns(2)

        # options = ['Por livro', 'Por capítulo']

        # selected = row[1].selectbox('Progresso', options)

        # if selected == options[0]:
        #     livro = df.groupby('status')['livro'].count().reset_index()
        #     fig = px.pie(
        #         livro,
        #         values='livro',
        #         names='status',
        #         title='Percentual lido por livros',
        #     )
        #     row[1].plotly_chart(fig, True)

        # if selected == options[1]:
        #     capitulos = df.sum()
        #     fig = px.pie(
        #         capitulos,
        #         values=[capitulos['capitulos'], capitulos['capitulos_lidos']],
        #         names=['Não Lidos', 'Lidos'],
        #         title='Percentual lido por capítulos',
        #     )
        #     row[1].plotly_chart(fig, True)

        #################################################################

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
