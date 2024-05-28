# import pandas as pd

# from planodeleituraanual.database import get_plano_tbl
# from planodeleituraanual.database import set_chapter_read

# from tinydb.operations import delete


if __name__ == '__main__':

    # tbl = get_plano_tbl()

    # for item in tbl.all():
    #     print(item.doc_id)
    #     tbl.update(delete('mesdia'), doc_ids=[item.doc_id])

    # popula usuario.db.json

    # df = pd.read_excel('biblia.ods', engine='odf')

    # index_list = [i for i in range(len(df)) if df['capitulos_lidos'][i] > 0]
    # index_list = [i for i in range(len(df)) if df['capitulos_lidos'][i] > 0]

    # print(index_list)

    # for i in index_list:
    #     print(df['livro'][i])
    #     for cap in range(1, df['capitulos_lidos'][i] + 1):
    #         set_chapter_read('_'.join([df['livro'][i], str(cap)]))

    # renomear arquivos acf
    # init = 27

    # for i in range(1, 40):
    #     # print(init + i)
    #     for filename in os.listdir('acf-json'):
    #         # print(filename)
    #         if 'at_book-{}_chapter-'.format(str(init + i)) in filename:
    #             # print(filename)
    #             print(i)
    #             os.rename(
    #                 os.path.join(os.getcwd(), 'acf-json', filename),
    #                 os.path.join(
    #                     os.getcwd(),
    #                     'acf-json',
    #                     filename.replace(
    #                         'at_book-{}_chapter-'.format(str(init + i)),
    #                         '{}_'.format(str(i)),
    #                     ),
    #                 ),
    #             )

    # init_correto = 39

    # for i in range(1, 28):
    #     # print(i)
    #     for filename in os.listdir('acf-json'):
    #         # print(filename)
    #         if 'nt_book-{}_chapter-'.format(str(i)) in filename:
    #             # print(filename)
    #             print(init_correto + i)
    #             os.rename(
    #                 os.path.join(os.getcwd(), 'acf-json', filename),
    #                 os.path.join(
    #                     os.getcwd(),
    #                     'acf-json',
    #                     filename.replace(
    #                         'nt_book-{}_chapter-'.format(str(i)),
    #                         '{}_'.format(str(init_correto + i)),
    #                     ),
    #                 ),
    #             )

    # remove book key dos jsons

    import json
    import os

    for filename in os.listdir('acf-json'):
        print(filename)

        f = open(os.path.join(os.getcwd(), 'acf-json', filename))

        data = json.load(f)
        del data['book']

        f = open(os.path.join(os.getcwd(), 'acf-json', filename), 'w')
        f.write(json.dumps(data))
        f.close()
