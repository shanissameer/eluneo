import sqlite3

def create_database():

    conn = sqlite3.connect("capsules.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS capsules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        message TEXT,
        unlock_date TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_capsule(title, message, unlock_date):

    conn = sqlite3.connect("capsules.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO capsules
        (title, message, unlock_date)
        VALUES (?, ?, ?)
        """,
        (title, message, str(unlock_date))
    )

    conn.commit()
    conn.close()


def get_capsules():

    conn = sqlite3.connect("capsules.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT title, message, unlock_date FROM capsules"
    )

    capsules = cursor.fetchall()

    conn.close()

    return capsules