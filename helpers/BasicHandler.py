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

    def _get_all(self):
        pass