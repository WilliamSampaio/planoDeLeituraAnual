import datetime as dt

from tinydb import TinyDB


def get_db(path) -> TinyDB:
    return TinyDB(path)


def get_table(table_name: str, db_instance: TinyDB) -> TinyDB:
    db_instance.default_table_name = table_name
    return db_instance


def get_db_plano():
    return get_db('plano.json')


def get_db_usuario():
    return get_db('usuario.db.json')


def get_plano_tbl():
    return get_table('plano', get_db_plano())


def get_usuario_tbl():
    return get_table('plano_usuario', get_db_usuario())


def get_usuario():
    return get_usuario_tbl().get(doc_id=1)


def get_plano_id(date: dt.date):
    cronograma = get_usuario()['cronograma']
    for item in cronograma:
        if item[1] == date.strftime('%Y-%m-%d'):
            return item[0]
    return None


def get_bread_daily(id):
    bread = get_plano_tbl().get(doc_id=1000)
    if bread is not None:
        return bread
    return None
