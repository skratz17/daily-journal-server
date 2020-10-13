from helpers import BasicHandler
from models import Concept

class ConceptHandler(BasicHandler):
    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM Concepts c
        """)

        results = cursor.fetchall()

        concepts = [ (Concept(**concept)).__dict__ for concept in results ]

        return concepts

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM Concepts c
        WHERE c.id = ?
        """, ( id, ))

        result = cursor.fetchone()

        concept = Concept(**result).__dict__
        
        return concept

    def _create(self, cursor, concept):
        cursor.execute("""
        INSERT INTO Concepts
            ( name )
        VALUES
            ( ? )
        """, ( concept['name'], ))

        id = cursor.lastrowid
        concept['id'] = id

        return concept

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE 
        FROM Concepts
        WHERE id = ?
        """, ( id, ))