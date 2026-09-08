from services.bible_manager import bible_man
from services.vod_manager import vod_man
from datetime import date


def vod() -> dict:
    retvar = {'book': '', 'chapter': 0, 'verse': 0, 'verse_text': ''}
    today = str(date.today())
    last_date = vod_man()

    return retvar