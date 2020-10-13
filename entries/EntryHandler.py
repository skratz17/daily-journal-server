from helpers import BasicHandler
from models import Entry

class EntryHandler(BasicHandler):
    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.moodId
        FROM Entries e
        """)

        results = cursor.fetchall()

        entries = [ (Entry(**entry)).__dict__ for entry in results ]

        return entries