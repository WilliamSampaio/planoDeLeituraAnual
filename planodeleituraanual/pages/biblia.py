from streamlit.delta_generator import DeltaGenerator

from planodeleituraanual.acf import get_books, get_chapter_count


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def index(tab: DeltaGenerator):

    livro = tab.selectbox('Livro:', get_books())

    tab.write('#### Capítulos')

    chapter_list = range(1, get_chapter_count(livro) + 1)

    # print(chunks(chapter_list, 10))

    # tab.write(chunks(chapter_list, 10))

    # capitulo = row_selects[1].selectbox('Capítulo:',['a','b'])
