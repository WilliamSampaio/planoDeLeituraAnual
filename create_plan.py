import datetime as dt

import streamlit as st
from dotenv import dotenv_values

import database as db

config = dotenv_values('.env')


def create_plan():
    st.set_page_config(config['APP_NAME'], ':book:')

    with st.form('create_plan_form'):

        st.header('Criar Novo Plano')
        st.subheader('Inicie um novo plano de leitura :book:')

        nome = st.text_input('Seu nome:', max_chars=100)

        data_inicio = st.date_input('Data inicio')

        submit = st.form_submit_button('Criar')

        if submit:

            if len(nome) == 0:
                st.error('Seu nome precisa ser informado!')
                st.stop()

            plano_len = len(db.get_plano_tbl().all())

            date_list = [
                data_inicio + dt.timedelta(days=x) for x in range(plano_len)
            ]

            st.write(date_list)

            st.balloons()
