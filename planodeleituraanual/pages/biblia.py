import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from planodeleituraanual import acf
from planodeleituraanual.database import is_chapter_read


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def index(tab: DeltaGenerator):

    if 'capitulo' not in st.session_state:
        st.session_state.capitulo = 1

    if 'expanded' not in st.session_state:
        st.session_state.expanded = True

    def set_capitulo(capitulo):
        st.session_state.capitulo = capitulo
        st.session_state.expanded = False

    def toogle_expanded():
        st.session_state.expanded = not st.session_state.expanded

    def voltar_capitulo():
        st.session_state.capitulo -= 1

    def avancar_capitulo():
        st.session_state.capitulo += 1

    livro = tab.selectbox(
        '**Livro**', acf.get_books(), on_change=toogle_expanded
    )

    chapter_expander = tab.expander('**Capítulos**', st.session_state.expanded)
    chapter_expander.divider()

    chapter_list = range(1, acf.get_chapter_count(livro) + 1)

    for sub_list in chunks(chapter_list, 10):
        btn_chapters = chapter_expander.columns(10, gap='large')
        for i in range(len(sub_list)):
            btn_chapters[i].button(
                '**{}**'.format(
                    ''.join(
                        [
                            str(sub_list[i]),
                            ' :white_check_mark:'
                            if is_chapter_read(f'{livro}_{str(sub_list[i])}')
                            else '',
                        ]
                    )
                ),
                f'btn_{livro.lower()}_{sub_list[i]}',
                on_click=set_capitulo,
                args=[sub_list[i]],
                use_container_width=True,
            )

    tab.divider()

    row_titulo = tab.columns([0.1, 1, 0.1])
    if st.session_state.capitulo > 1:
        row_titulo[0].button(
            f'### :arrow_backward: {st.session_state.capitulo - 1}',
            key='btn_voltar_cap',
            on_click=voltar_capitulo,
            use_container_width=True,
        )
    row_titulo[1].markdown(
        '#### <center>{}<center>'.format(
            f'{livro} {st.session_state.capitulo}'
        ),
        True,
    )
    if st.session_state.capitulo < acf.get_chapter_count(livro):
        row_titulo[2].button(
            f'### {st.session_state.capitulo + 1} :arrow_forward:',
            key='btn_avancar_cap',
            on_click=avancar_capitulo,
            use_container_width=True,
        )

    conteudo = acf.get_chapter(
        acf.get_book_id(livro), st.session_state.capitulo
    )

    if conteudo is not None:

        cols = tab.columns(2)
        verses_col = chunks(
            conteudo['verses'], int(len(conteudo['verses']) / 1.7)
        )

        for verse in next(verses_col):
            for key, value in verse.items():
                cols[0].html('{}. {}'.format(key, value))

        for verse in next(verses_col):
            for key, value in verse.items():
                cols[1].html('{}. {}'.format(key, value))
