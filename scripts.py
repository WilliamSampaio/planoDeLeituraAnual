import pandas as pd

# from planodeleituraanual.database import get_plano_tbl
from planodeleituraanual.database import set_chapter_read

# from tinydb.operations import delete


if __name__ == '__main__':

    # tbl = get_plano_tbl()

    # for item in tbl.all():
    #     print(item.doc_id)
    #     tbl.update(delete('mesdia'), doc_ids=[item.doc_id])

    # popula usuario.db.json

    df = pd.read_excel('biblia.ods', engine='odf')

    index_list = [i for i in range(len(df)) if df['capitulos_lidos'][i] > 0]
    index_list = [i for i in range(len(df)) if df['capitulos_lidos'][i] > 0]

    print(index_list)

    for i in index_list:
        print(df['livro'][i])
        for cap in range(1, df['capitulos_lidos'][i] + 1):
            set_chapter_read('_'.join([df['livro'][i], str(cap)]))
