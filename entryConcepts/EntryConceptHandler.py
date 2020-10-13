import entryConcepts
from helpers import BasicHandler
from models import EntryConcept

class EntryConceptHandler(BasicHandler):
    def _get_all(self, cursor):
        cursor.execute("""
        SELECT 
            ec.id,
            ec.entryId,
            ec.conceptId
        FROM EntryConcepts ec
        """)

        results = cursor.fetchall()

        entryConcepts = [ (EntryConcept(**entryConcept)).__dict__ for entryConcept in results ]

        return entryConcepts

    def _create(self, cursor, entryConcept):
        cursor.execute("""
        INSERT INTO EntryConcepts
            ( entryId, conceptId )
        VALUES
            ( ?, ? )
        """, ( entryConcept['entryId'], entryConcept['conceptId'] ))

        id = cursor.lastrowid
        entryConcept['id'] = id

        return entryConcept

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE
        FROM EntryConcepts
        WHERE id = ?
        """, ( id, ))