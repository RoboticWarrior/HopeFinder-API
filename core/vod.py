from data.bible_read import bible_read
from data.vod_manager import vod_man
from datetime import date


def vod() -> dict:
    retvar = {'book': '', 'chapter': 0, 'verse': 0, 'verse_text': ''}
    today = str(date.today())
    last_date = vod_man()

    return retvar