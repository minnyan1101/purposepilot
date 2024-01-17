import sqlite3
from .create_db import create_table


def drop_tables(conn):
    tables = ("User", "Purpose", "Action", "Review", "Session")
    cur = conn.cursor()
    for table in tables:
        cur.execute(f"DROP TABLE IF EXISTS {table}")
    conn.commit()


def main():
    conn = sqlite3.connect('purpose_pilot.db')

    drop_tables(conn)
    create_table()
    
    cur = conn.cursor()
    data = [
        (
            'test_1', 
            '-CpLk4aI4LBlB35kO7CypOAp7q2DPYGAonfc4NciG9w;5a97891464406522ba9982d418945987505dbe5d6a485fb20e5cd7eebef79ac7b097de61eed3e30be3e6f62c6c3b47b2571fe901a0d3096a6de9662a9fdc79cb', 
            '2024-01-14T16:46:25.498268+00:00',
            '2025-01-14T16:46:25.498268+00:00',
            ''
        ),
        (
            'test_2', 
            'YjT-ZvmoSmSSWXsi4TZqb3r-widT9sJkJD-j9VraPE4;a1a92a5bbff68d7eeaeb50288446a92b40bb4468db86f071bb2f83ae9c6590c27922350a5f50a2aab9f33b92f57448ae8d3c11667b8eb8c18af381f49bba71fc', 
            '2024-01-14T16:46:25.498268+00:00',
            '2025-01-14T16:46:25.498268+00:00',
            ''
        ),
    ]
    cur.executemany(
        '''
        INSERT INTO User VALUES(?, ?, ?, ?, ?)
        ''',
        data
        )

    conn.commit()
    
    data = [
        (
            "test_1",
            "てすと１",
            "てすとでーた１の説明",
            "2024-01-14T16:46:25.498268+00:00",
            "2024-01-14T16:46:25.498268+00:00",
            False,
            None,
        ),
        (
            "test_1",
            "てすと2",
            "てすとでーた2の説明",
            "2024-01-14T16:46:25.498268+00:00",
            "2024-01-14T16:46:25.498268+00:00",
            True,
            "2024-01-14T16:46:25.498268+00:00",
        ),
    ]
    cur.executemany(
        """
        INSERT into Purpose (user_id, title, description, created_at, due_at, is_completed, completed_at)
            values (?, ?, ?, ?, ?, ?, ?)
        """,
        data
        )
    
    conn.commit()
    
    data = {
        (
            "test_1",
            1,
            "てすとでーた１",
            "2024-01-14T16:46:25.498268+00:00",
            "2024-01-14T16:46:25.498268+00:00",
        ),
        (
            "test_1",
            1,
            "てすとでーた2",
            "2024-01-14T16:46:25.498268+00:00",
            "2024-01-14T16:46:25.498268+00:00",
        ),
        (
            "test_1",
            1,
            "てすとでーた3",
            "2024-01-14T16:46:25.498268+00:00",
            "2024-01-14T16:46:25.498268+00:00",
        )
    }

    cur.executemany(
        """
        INSERT into Action (user_id, purpose_id, action_detail, started_at, finished_at)
            values (?,?,?,?,?)
        """,
        data
        )
    
    conn.commit()


if __name__ == '__main__':
    main()