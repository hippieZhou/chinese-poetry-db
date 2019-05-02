"""
类别：诗-作者
"""

import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "shi_tangsong_author" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" TEXT,
  "desc" TEXT
);
'''
    print('\r\n诗-唐宋-作者 正在初始化...')
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        author_data = os.path.join(path, 'authors.song.json')
        print('\t', author_data)
        save_author(cur, author_data)
        author_tang_data = os.path.join(path, 'authors.tang.json')
        print('\t', author_tang_data)
        save_author(cur, author_tang_data)
        conn.commit()
        print('诗-唐宋-作者 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def save_author(cur, file):
    with open(file, 'r', encoding='UTF-8') as f:
        author_dict = json.load(f)
        items = [(item['name'], item['desc']) for item in author_dict]
        cur.executemany(
            "insert into shi_tangsong_author(name, desc) values (?,?)", items)
