import json
import os

import pandas as pd


def load_biblia_df():
    return pd.read_json(os.path.join(os.getcwd(), 'biblia.df.json'))


def get_book_id(book: str):
    df = load_biblia_df()
    result = [df['id'][i] for i in range(len(df)) if df['livro'][i] == book]
    if len(result) > 0:
        return result[0]
    return None


def get_chapter(book_id, chapter_id):
    if not book_id or not chapter_id:
        return None
    try:
        f = open(
            os.path.join(
                os.getcwd(),
                'acf-json',
                '{}_{}.json'.format(book_id, chapter_id),
            )
        )
        return json.load(f)
    except FileNotFoundError as e:
        print(str(e))
    return None
