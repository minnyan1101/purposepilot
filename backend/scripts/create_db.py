import sqlite3


def main():
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
            purpose_id INT AUTO INCREMENT NOT NULL, --目標ID
            user_id TEXT NOT NULL, --ユーザーID
            title TEXT NOT NULL, --目標タイトル
            description TEXT NOT NULL, --目標内容
            created_at DATETIME NOT NULL, --作成日時
            due_at DATETIME, --期限
            is_completed BOOL NOT NULL, --完了フラグ
            completed_at DATETIME, --完了日時
            PRIMARY KEY (purpose_id,user_id)
            FOREIGN KEY (user_id) references User(user_id)
            )''')
    conn.commit()

    cur.execute('''
            CREATE TABLE Action (
            action_id INT AUTO INCREMENT NOT NULL, --行動ID
            user_id TEXT NOT NULL, --ユーザーID
            purpose_id INT NOT NULL, --目標ID
            action_detail TEXT NOT NULL, --行動内容
            run_duration_sec INT NOT NULL, --実行時間
            started_at DATETIME NOT NULL, --開始日時
            finished_at DATETIME, --終了日時
            PRIMARY KEY (action_id,user_id)
            FOREIGN KEY (user_id) references Users(user_id),
            FOREIGN KEY (purpose_id) references Purpose(purpose_id)
            )''')
    conn.commit()

    cur.execute('''
            CREATE TABLE Review (
            review_id INT AUTO INCREMENt, --振り返りID
            user_id TEXT, --ユーザーID
            purpose_id INT, --目標ID
            question_id INT, --質問ID
            reviewed_at DATETIME NOT NULL, --振り返り日時
            first_question_rating DOUBLE NOT NULL, --1問目の評価値
            second_question_rating DOUBLE NOT NULL, --2問目の評価値
            third_question_rating DOUBLE NOT NULL, --3問目の評価値
            PRIMARY KEY (review_id)
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


if __name__ == "__main__":
    main()
