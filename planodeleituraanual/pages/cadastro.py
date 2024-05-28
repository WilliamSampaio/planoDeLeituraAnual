import datetime as dt
import time

import streamlit as st
from dotenv import dotenv_values

import planodeleituraanual.database as db

from ..shutdown import shutdown

config = dotenv_values('.env')


def index():

    st.set_page_config(config['APP_NAME'], ':book:')

    shutdown()

    with st.form('create_plan_form'):

        st.header('Criar Novo Plano')
        st.subheader('Inicie um novo plano de leitura :book:')

        nome = st.text_input('Seu nome:', max_chars=100)

        data_inicio = st.date_input('Data inicio', format='DD/MM/YYYY')

        submit = st.form_submit_button('Criar')

        if submit:

            if len(nome) == 0:
                st.error('Seu nome precisa ser informado!')
                st.stop()

            plano_len = len(db.get_plano_tbl().all())

            date_list = [
                dt.date(2023, 1, 1) + dt.timedelta(days=x)
                for x in range(plano_len)
            ]

            cronograma = []
            for index in range(len(date_list)):
                cronograma.append(
                    [str(index + 1), date_list[index].strftime('%m-%d')]
                )

            db.get_usuario_tbl().insert(
                {
                    'nome': nome.upper(),
                    'inicio': data_inicio.strftime('%Y-%m-%d'),
                    'cronograma': cronograma,
                    'lidos': [],
                }
            )

            st.balloons()
            time.sleep(2)
            st.rerun()
