from helpers import BasicHandler
from models import Entry, Mood

class EntryHandler(BasicHandler):
    def __build_expanded_entry_from_row(self, row):
        entry = Entry(row['id'], row['date'], row['entry'], row['moodId'])

        mood = Mood(row['moodId'], row['mood_value'], row['mood_label'])

        entry.mood = mood.__dict__

        return entry.__dict__

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.moodId,
            m.value mood_value,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.moodId
        """)

        results = cursor.fetchall()

        entries = [ self.__build_expanded_entry_from_row(row) for row in results ]

        return entries

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.moodId,
            m.value mood_value,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.moodId
        WHERE e.id = ?
        """, ( id, ))

        result = cursor.fetchone()

        entry = self.__build_expanded_entry_from_row(result)

        return entry

    def _create(self, cursor, entry):
        cursor.execute("""
        INSERT INTO Entries
            ( date, entry, moodId )
        VALUES
            ( ?, ?, ? )
        """, ( entry['date'], entry['entry'], entry['moodId'] ))

        id = cursor.lastrowid
        entry['id'] = id

        return entry

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE 
        FROM Entries
        WHERE id = ?
        """, ( id, ))