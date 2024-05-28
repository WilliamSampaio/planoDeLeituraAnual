import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from planodeleituraanual import acf


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def index(tab: DeltaGenerator):

    if 'capitulo' not in st.session_state:
        st.session_state.capitulo = 1

    def set_capitulo(capitulo):
        st.session_state.capitulo = capitulo

    livro = tab.selectbox('Livro:', acf.get_books())

    tab.write('#### Capítulos')

    chapter_list = range(1, acf.get_chapter_count(livro) + 1)

    for sub_list in chunks(chapter_list, 10):
        btn_chapters = tab.columns(10)
        for i in range(len(sub_list)):
            btn_chapters[i].button(
                '**{}**'.format(str(sub_list[i])),
                '{}_{}'.format(livro, sub_list[i]),
                on_click=set_capitulo,
                args=[sub_list[i]],
            )
    tab.divider()
    conteudo = acf.get_chapter(
        acf.get_book_id(livro), st.session_state.capitulo
    )
    if conteudo is not None:
        for verse in conteudo['verses']:
            for key, value in verse.items():
                tab.markdown(
                    '{}. {}'.format(key, value), unsafe_allow_html=True
                )

    # print(chunks(chapter_list, 10))

    # tab.write(chunks(chapter_list, 10))

    # capitulo = row_selects[1].selectbox('Capítulo:',['a','b'])
