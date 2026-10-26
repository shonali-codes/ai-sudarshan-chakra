import sqlite3
from datetime import datetime

DB_NAME = "events.db"


def init_db():
    """
    Create governance event table if it does not exist.
    """

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS governance_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prompt TEXT,
            risk_score INTEGER,
            decision TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def log_event(
    prompt,
    risk_score,
    decision
):
    """
    Store governance event.
    """

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO governance_events
        (
            timestamp,
            prompt,
            risk_score,
            decision
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            prompt,
            risk_score,
            decision
        )
    )

    conn.commit()
    conn.close()


def get_events():
    """
    Return governance events.
    """

    conn = sqlite3.connect(DB_NAME)

    rows = conn.execute(
        """
        SELECT *
        FROM governance_events
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    return rows