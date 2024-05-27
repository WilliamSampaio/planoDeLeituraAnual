from database import get_plano_tbl
from tinydb.operations import delete


if __name__ == '__main__':

    tbl = get_plano_tbl()

    for item in tbl.all():
        print(item.doc_id)
        tbl.update(delete('mesdia'), doc_ids=[item.doc_id])
