import sqlite3


def bible_man(book: str, chapter: int, verse: int) -> str:
    retvar = ''
    connection = sqlite3.connect('kjv.sqlite')

    with connection as db:
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM {book}')

    connection.close()

    return retvar