import pandas as pd
import streamlit as st
from dotenv import dotenv_values

import database as db
from create_plan import create_plan


@st.cache_data
def load_biblia_df():
    return pd.read_json('biblia.df.json')


if __name__ == '__main__':

    if db.get_usuario() is None:
        create_plan()
    else:

        config = dotenv_values('.env')

        st.set_page_config(config['APP_NAME'], ':book:', 'wide')

        usuario = db.get_usuario()

        st.write('# {}'.format(config['APP_NAME']))

        container = st.container()

        row = container.columns(2)

        row[0].write('## Leitura')

        data = row[0].date_input('Data Específica:', format='DD/MM/YYYY')

        leituras = db.get_bread_daily(data)

        row[0].divider()

        row_leituras = row[0].columns([1.5, 0.5])
        for item in leituras:
            row_leituras[0].write(item.replace('_', ' '))
            row_leituras[1].toggle(
                'Marque como Lido',
                value=db.is_chapter_read(item),
                key=item,
                on_change=db.set_chapter_read,
                args=[item],
            )

        row[1].write('## Progresso')

        options = ['Por livro', 'Por capítulo']

        selected = row[1].selectbox('Acompanhar Por:', options)

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

        # df = pd.read_excel('biblia.ods', engine='odf')
        # df = df.drop(['pagina_inicial', 'quantidade_paginas'], axis=1)
        # df['status'] = np.where(
        #     df['capitulos'] == df['capitulos_lidos'], 'Lidos', 'Não Lidos'
        # )

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
