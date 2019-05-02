"""
类别：诗经
"""
import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "shijing" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" text,
  "chapter" text,
  "section" TEXT,
  "content" TEXT
);
'''
    print('\r\n诗经 正在初始化...')
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        shijing_data = os.path.join(path, 'shijing.json')
        if os.path.exists(shijing_data) is None:
            print('诗经 数据文件不存在')
            return
        print('\t', shijing_data)
        with open(shijing_data, 'r', encoding='UTF-8') as f:
            data_dict = json.load(f)
            items = [(str(item['title']), str(item['chapter']), str(item['section']), str(item['content']))
                     for item in data_dict]
            cur.executemany(
                "insert into shijing(title, chapter, section, content) values (?,?,?,?)", items)
        conn.commit()
        print('诗经 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()
