"""
类别：四书五经
"""
import sqlite3
import os
import json


def make_db(db, path):
    sql = '''
CREATE TABLE IF NOT EXISTS "sishuwujing" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "chapter" TEXT,
  "paragraphs" TEXT,
  "category" TEXT
);
    '''
    print("\r\n四书五经 正在初始化...")
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        daxue = os.path.join(path, 'daxue.json')
        json = json_data(daxue)
        items = [(str(json['chapter']), str(json['paragraphs']), '大学'), ]
        cur.executemany(
            "insert into sishuwujing(chapter, paragraphs, category) values (?,?,?)", items)

        mengzi = os.path.join(path, 'mengzi.json')
        json = json_data(mengzi)
        items = [(str(item['chapter']), str(item['paragraphs']), '孟子')
                 for item in json]
        cur.executemany(
            "insert into sishuwujing(chapter, paragraphs, category) values (?,?,?)", items)

        zhongyong = os.path.join(path, 'zhongyong.json')
        json = json_data(zhongyong)
        items = [(str(json['chapter']), str(json['paragraphs']), '中庸'), ]
        cur.executemany(
            "insert into sishuwujing(chapter, paragraphs, category) values (?,?,?)", items)
            
        conn.commit()
        print('四书五经 数据处理完毕.')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def json_data(file):
    if os.path.exists(file):
        print('\t', file)
        with open(file, 'r', encoding='UTF-8') as f:
            data_json = json.load(f)
            return data_json
