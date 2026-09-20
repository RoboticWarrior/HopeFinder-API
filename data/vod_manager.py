# import sqlite3


# def vod_man(new_verse: str = 'None') -> list:
#     retvar = []
#     db_con = sqlite3.connect('data/vod_data.db')

#     with db_con as db:
#         cur = db.cursor()
#         cur.execute('''
#         CREATE TABLE IF NOT EXISTS verses (
#                     date TEXT PRIMARY KEY, 
#                     book TEXT NOT NULL, 
#                     chapter INTEGER NOT NULL, 
#                     verse INTEGER NOT NULL,
#                     verse_text TEXT NOT NULL
#                     )''')

#         if new_verse != 'None':
#             cur.execute('')

#         cur.execute('SELECT * FROM verses')
#         retvar = cur.fetchall()

#     db_con.close()

#     return retvar
from data.bible_read import bible_read


def vod_man() -> dict:
    

    return {}