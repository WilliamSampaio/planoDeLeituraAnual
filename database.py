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


def get_bread_daily(date: dt.date = dt.date.today()) -> dict:
    mes_dia = date.strftime('%m-%d')
    if mes_dia == '02-29':
        return None
    usuario = get_usuario()
    if usuario is None:
        return None
    cronograma = usuario['cronograma']
    for item in cronograma:
        if item[1] == mes_dia:
            bread = get_plano_tbl().get(doc_id=item[0])
            if bread is not None:
                return bread['leituras']
    return None
