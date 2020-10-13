import sqlite3
import json

from models import Entry

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.moodId
        FROM Entries e
        """)

        results = db_cursor.fetchall()

        entries = [ (Entry(**entry)).__dict__ for entry in results ]

        return entries