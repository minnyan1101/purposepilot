import sqlite3


def main():
    conn = sqlite3.connect('purpose_pilot.db')

    cur = conn.cursor()
    data = [
        (
            'test_1', 
            '-CpLk4aI4LBlB35kO7CypOAp7q2DPYGAonfc4NciG9w;5a97891464406522ba9982d418945987505dbe5d6a485fb20e5cd7eebef79ac7b097de61eed3e30be3e6f62c6c3b47b2571fe901a0d3096a6de9662a9fdc79cb', 
            '2024-01-14T16:46:25.498268',
            '2025-01-14T16:46:25.498268',
            ''
        ),
        (
            'test_2', 
            'YjT-ZvmoSmSSWXsi4TZqb3r-widT9sJkJD-j9VraPE4;a1a92a5bbff68d7eeaeb50288446a92b40bb4468db86f071bb2f83ae9c6590c27922350a5f50a2aab9f33b92f57448ae8d3c11667b8eb8c18af381f49bba71fc', 
            '2024-01-14T16:46:25.498268',
            '2025-01-14T16:46:25.498268',
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


if __name__ == '__main__':
    main()