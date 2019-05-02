"""
类别：词-宋-作者
"""

import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "ci_song_author" (
"id" INTEGER NOT NULL,
"name" TEXT,
"desc" TEXT,
"short_desc" TEXT,
PRIMARY KEY ("id")
);
    '''
    print('\r\n词-宋-作者 正在初始化...')
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        author_data = os.path.join(path, 'author.song.json')
        if os.path.exists(author_data) is None:
            print('词-宋-作者 数据文件不存在')
            return
        print('\t', author_data)
        with open(author_data, 'r', encoding='UTF-8') as f:
            author_dict = json.load(f)
            items = [(str(item['name']), str(item['description']), str(item['short_description']))
                     for item in author_dict]
            cur.executemany(
                "insert into ci_song_author(name, desc, short_desc) values (?,?,?)", items)
        conn.commit()
        print('词-宋-作者 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()
