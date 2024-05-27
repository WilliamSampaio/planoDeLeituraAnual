import datetime as dt

from tinydb import Query, TinyDB


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


def get_bread_daily(date: dt.date = dt.date.today()) -> dict:
    mesdia = date.strftime('%m-%d')
    if mesdia == '02-29':
        return None
    query = Query()
    return get_plano_tbl().search(query.mesdia == mesdia)[0]
