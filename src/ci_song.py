"""
类别：词-宋
"""

import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "ci_song" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"author_id" INTEGER,
"author" TEXT,
"paragraphs" TEXT,
"rhythmic" TEXT
);
    '''
    print('\r\n词-宋 正在初始化...')
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        for i in range(0, 21000, 1000):
            ci_data = os.path.join(path, 'ci.song.{0}.json'.format(i))
            if os.path.exists(ci_data):
                print('\t', ci_data)
                with open(ci_data, 'r', encoding='UTF-8') as f:
                    data_dict = json.load(f)
                    items = [(str(item['author']), str(item['paragraphs']), str(item['rhythmic']))
                             for item in data_dict]
                    for item in items:
                        one = cur.execute("select * from ci_song_author where name= '{0}'".format(
                            str(item[0]).lstrip())).fetchone()
                        author_id = None
                        if one:
                            author_id = one[0]
                        cur.execute("insert into ci_song(author_id, author, paragraphs, rhythmic) values (?,?,?,?)", (
                            author_id, item[0], item[1], item[2]))
                        conn.commit()
        print('词-宋 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()
