import datetime as dt
import os

from dotenv import dotenv_values
from tinydb import TinyDB

config = dotenv_values(os.path.join(os.getcwd(), '.env'))


if config['APP_ENV'] == 'dev':
    dir = os.getcwd()
elif config['APP_ENV'] == 'prod':
    dir = os.path.join(os.environ.get('HOME'), '.planodeleituraanual')


def get_db(path) -> TinyDB:
    return TinyDB(path)


def get_table(table_name: str, db_instance: TinyDB) -> TinyDB:
    db_instance.default_table_name = table_name
    return db_instance


def get_db_plano():
    return get_db(os.path.join(os.getcwd(), 'plano.json'))


def get_db_usuario():
    return get_db(os.path.join(dir, 'usuario.db.json'))


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


def count_chapters_read(book: str) -> int:
    usuario = get_usuario()
    if usuario is None:
        return None
    return len(
        [x.split('_')[1] for x in usuario['lidos'] if x.split('_')[0] == book]
    )


def is_chapter_read(chapter: str):
    usuario = get_usuario()
    if usuario is None:
        return False
    return True if chapter in usuario['lidos'] else False


def set_chapter_read(chapter: str):
    usuario = get_usuario()
    if usuario is None:
        return None
    lidos = usuario['lidos']
    if chapter in lidos:
        lidos.remove(chapter)
    else:
        lidos.append(chapter)
    usuario['lidos'] = lidos
    return get_usuario_tbl().update(usuario, doc_ids=[1])
