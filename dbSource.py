import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS flights(id INTEGER PRIMARY KEY, company text, flight text, "
                         "departureFrom text, departure text, arrivalTo text, arrival text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM flights")
        rows = self.cur.fetchall()
        return rows

    def insert(self, company, flight, departureFrom, departure, arrivalTo, arrival):
        self.cur.execute("INSERT INTO flights VALUES (NULL, ?, ?, ?, ?, ?, ?)", (company, flight, departureFrom,
                                                                                 departure, arrivalTo, arrival))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM flights WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, company, flight, departureFrom, departure, arrivalTo, arrival):
        self.cur.execute("UPDATE flights SET company = ?, flight = ?, departureFrom = ?, departure = ?, arrivalTo = ?, "
                         "arrival = ? WHERE id = ?", (company, flight, departureFrom, departure, arrivalTo, arrival,
                                                      id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('')