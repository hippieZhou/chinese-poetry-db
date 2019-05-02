"""
类别：论语
"""
import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "lunyu" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "chapter" TEXT,
  "paragraphs" TEXT
);
'''
    print('\r\n论语 正在初始化...')
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        lunyu_data = os.path.join(path, 'lunyu.json')
        if os.path.exists(lunyu_data) is None:
            print('论语 数据文件不存在')
            return
        print('\t', lunyu_data)
        with open(lunyu_data, 'r', encoding='UTF-8') as f:
            data_dict = json.load(f)
            items = [(str(item['chapter']), str(item['paragraphs']))
                     for item in data_dict]
            cur.executemany(
                "insert into lunyu(chapter, paragraphs) values (?,?)", items)
        conn.commit()
        print('论语 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()
