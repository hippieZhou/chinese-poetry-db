"""
类别：诗
"""

import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "shi_tangsong" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "author_id" INTEGER,
  "author" TEXT,
  "title" TEXT,
  "paragraphs" TEXT,
  "strains" TEXT
);
'''
    print('\r\n诗-唐宋 正在初始化...')
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        for i in range(0, 254000, 1000):
            shi_file = os.path.join(path, 'poet.song.{0}.json'.format(i))
            save_data(cur, shi_file)
        for i in range(0, 57000, 1000):
            shi_file = os.path.join(path, 'poet.tang.{0}.json'.format(i))
            save_data(cur, shi_file)
        conn.commit()
        print('诗-唐宋 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def save_data(cur, file):
    if os.path.exists(file):
        print('\t', file)
        with open(file, 'r', encoding='UTF-8') as f:
            shi_data = json.load(f)
            items = [(str(item['author']), str(item['paragraphs']), str(item['strains']),
                      str(item['title'])) for item in shi_data]
            for item in items:
                sql = "select * from shi_tangsong_author where name = '{0}'".format(
                    item[0].lstrip())
                one = cur.execute(sql).fetchone()
                author_id = None
                if one:
                    author_id = one[0]
                cur.execute("insert into shi_tangsong(author, paragraphs, strains, title, author_id) values (?,?,?,?,?)", (
                    item[0], item[1], item[2], item[3], author_id))
