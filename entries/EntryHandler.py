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

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.moodId
        FROM Entries e
        WHERE e.id = ?
        """, ( id, ))

        result = cursor.fetchone()

        entry = Entry(**result).__dict__

        return entry

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE 
        FROM Entries
        WHERE id = ?
        """, ( id, ))