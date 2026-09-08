import sqlite3


def bible_man(book: str, chapter: int, verse: int) -> dict:
    retvar = {'book': '', 'chapter': 0, 'verse': 0, 'verse_text': ''}
    connection = sqlite3.connect('bible.db')

    with connection as db:
        cursor = db.cursor()

    return retvar