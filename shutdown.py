import os
import time

import psutil
import streamlit as st
from dotenv import dotenv_values

config = dotenv_values('.env')


def shutdown():
    if 'shutdown' not in st.session_state:
        st.session_state['shutdown'] = False
    if st.session_state['shutdown'] is False:
        return
    st.set_page_config(config['APP_NAME'], ':book:', layout='wide')
    st.markdown(
        '### <center style="width: 77%;margin-left:auto;margin-right:auto;">Não se aparte da tua boca o livro desta lei; antes medita nele dia e noite, para que tenhas cuidado de fazer conforme a tudo quanto nele está escrito; porque então farás prosperar o teu caminho, e serás bem-sucedido. Não to mandei eu? Esforça-te, e tem bom ânimo; não temas, nem te espantes; porque o Senhor teu Deus é contigo, por onde quer que andares.</center>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '### <center style="width: 77%;margin-left:auto;margin-right:auto;">Josué 1:8-9</center>',
        unsafe_allow_html=True,
    )
    time.sleep(2)
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()


def btn_shutdown():
    st.divider()
    exit_btn = st.button('Sair')
    if exit_btn:
        st.session_state['shutdown'] = True
        st.rerun()
