from helpers import BasicHandler
from models import Mood

class MoodHandler(BasicHandler):
    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            m.id,
            m.label,
            m.value
        FROM Moods m
        """)

        results = cursor.fetchall()

        moods = [ (Mood(**mood)).__dict__ for mood in results ]

        return moods