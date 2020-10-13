import sqlite3
import json

class BasicHandler():
    def __exec_query(self, callback):
        with sqlite3.connect("./dailyjournal.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            return callback(cursor)

    def get_all(self):
        result = self.__exec_query(lambda cursor: self._get_all(cursor))
        return json.dumps(result)

    def get_by_id(self, id):
        result = self.__exec_query(lambda cursor: self._get_by_id(cursor, id))
        return json.dumps(result)

    def create(self, obj):
        result = self.__exec_query(lambda cursor: self._create(cursor, obj))
        return json.dumps(result)

    def delete(self, id):
        self.__exec_query(lambda cursor: self._delete(cursor, id))

    def _get_all(self, cursor):
        pass

    def _get_by_id(self, cursor, id):
        pass

    def _create(self, cursor, obj):
        pass

    def _delete(self, cursor, id):
        pass