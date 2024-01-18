import sqlite3


def create_table():
    conn = sqlite3.connect('purpose_pilot.db')
    cur = conn.cursor()

    cur.execute('''
            CREATE TABLE User (
            user_id TEXT NOT NULL, --ユーザーID
            hash TEXT NOT NULL, --ハッシュ済みパスワード
            created_at DATETIME NOT NULL, --作成日時
            updated_at DATETIME NOT NULL, --更新日時
            avater_image_url TEXT NOT NULL DEFAULT 0, --アバター画像URL
            PRIMARY KEY (user_id)
            )''')
    conn.commit()

    cur.execute('''
            CREATE TABLE Purpose (
            purpose_id INTEGER PRIMARY KEY AUTOINCREMENT, --目標ID
            user_id TEXT NOT NULL, --ユーザーID
            title TEXT NOT NULL, --目標タイトル
            description TEXT NOT NULL, --目標内容
            created_at DATETIME NOT NULL, --作成日時
            due_at DATETIME, --期限
            is_completed BOOL NOT NULL, --完了フラグ
            completed_at DATETIME, --完了日時
            FOREIGN KEY (user_id) references User(user_id)
            )''')
    conn.commit()

    cur.execute('''
            CREATE TABLE Action (
            action_id INTEGER PRIMARY KEY AUTOINCREMENT, --行動ID
            user_id TEXT NOT NULL, --ユーザーID
            purpose_id INT NOT NULL, --目標ID
            action_detail TEXT NOT NULL, --行動内容8
            started_at DATETIME NOT NULL, --開始日時
            finished_at DATETIME, --終了日時
            FOREIGN KEY (user_id) references Users(user_id),
            FOREIGN KEY (purpose_id) references Purpose(purpose_id)
            )''')
    conn.commit()

    cur.execute('''
            CREATE TABLE Review (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT, --振り返りID
            user_id TEXT, --ユーザーID
            purpose_id INT, --目標ID
            question_id INT, --質問ID
            reviewed_at DATETIME NOT NULL, --振り返り日時
            first_question_rating DOUBLE NOT NULL, --1問目の評価値
            second_question_rating DOUBLE NOT NULL, --2問目の評価値
            third_question_rating DOUBLE NOT NULL, --3問目の評価値
            FOREIGN KEY (user_id) references Users(user_id),
            FOREIGN KEY (purpose_id) references Purpose(purpose_id)
            )''')
    conn.commit()

    cur.execute('''
            CREATE TABLE Session (
            session_id TEXT, --セッションID
            user_id TEXT NOT NULL, --ユーザーID
            issued_at DATETIME NOT NULL, --発行日時
            expired_at DATETIME NOT NULL, --有効期限
            PRIMARY KEY (session_id)
            FOREIGN KEY (user_id) references Users(user_id)
            )''')
    conn.commit()


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
            'QZ2ki-1cWDFqExS_MIh-8QcvuqlOOc7mcvsOJ9aZUT8;a15df193f588f29a3a25c02602eb009e192eae48811bda89b8174a25d6a20c6b8e1a8d3a654e676bbbccd6946a81e4ec314e868d64931d1796e0080f95f12e3d',
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
