import sqlite3


class SQLiteRepo:
    def __init__(self, db: str = 'example.db'):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def create_schema(self):
        with self.conn:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
            ''')

    def generate_fake_users(self):
        with self.conn:
            self.cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 28)")
            self.cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 35)")
            self.cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 40)")
            self.cursor.execute("INSERT INTO users (name, age) VALUES ('David', 25)")
            self.conn.commit()

    def get_user_by_age(self, age: int) -> list[tuple[str, int]]:
        with self.conn:
            self.cursor.execute("SELECT * FROM users WHERE age > ?", (age,))
            results = self.cursor.fetchall()
        return results