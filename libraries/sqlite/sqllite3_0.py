import sqlite3


class SQLite(object):
    def __init__(self, file='demodatabase.bd'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


with SQLite() as c:
    c.execute('''CREATE TABLE stocks
        (date text, trans text, symbol text, qty real, price real)''')
    # insert a record/row
    c.execute("INSERT INTO stocks VALUES ('2006-03-12', 'buy', 'RHAT', 100, 35.90)")
