import numpy as np
import streamlit as st
from dotenv import dotenv_values

import planodeleituraanual.database as db
from planodeleituraanual.functions import load_biblia_df
from planodeleituraanual.pages import cadastro, home, progresso
from planodeleituraanual.shutdown import btn_shutdown, shutdown


def create_app():

    config = dotenv_values('.env')

    if db.get_usuario() is None:
        cadastro.index()
    else:
        st.set_page_config(config['APP_NAME'], ':book:', 'wide')

        shutdown()

        df = load_biblia_df()

        df['capitulos_lidos'] = [
            db.count_chapters_read(x) for x in df['livro']
        ]

        df['status'] = np.where(
            df['capitulos'] == df['capitulos_lidos'], True, False
        )

        st.session_state.biblia_df = df

        st.header(
            '{}'.format(
                ' '.join(
                    [
                        '({}) '.format(config['APP_ENV'])
                        if config['APP_ENV'] != 'prod'
                        else '',
                        config['APP_NAME'],
                    ]
                )
            )
        )

        tabs = st.tabs(['Home', 'Progresso'])

        home.index(tabs[0])
        progresso.index(tabs[1])

    btn_shutdown()
