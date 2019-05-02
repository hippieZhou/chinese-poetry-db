import argparse
import sqlite3
import os


def usage():
    parser = argparse.ArgumentParser()
    parser.description = '一键生成古诗词数据库文件'
    parser.add_argument("-n", nargs='?', help="数据库名称",
                        default="default.sqlite3")
    return parser.parse_args()


def work(name):
    db = os.path.join(os.getcwd(), name)
    if os.path.exists(db):
        os.remove(db)

    dataPath = os.path.join(os.getcwd(), 'data')

    # ci = os.path.join(dataPath, 'ci')
    # from src.ci_song_author import make_db as ci_song_author_make_db
    # ci_song_author_make_db(db, ci)
    # from src.ci_song import make_db as ci_song_data_make_db
    # ci_song_data_make_db(db, ci)

    # lunyu = os.path.join(dataPath, 'lunyu')
    # from src.lunyu import make_db as lunyu_make_db
    # lunyu_make_db(db, lunyu)

    shi = os.path.join(dataPath, 'json')
    from src.shi_tangsong_author import make_db as shi_tangsong_author_make_db
    shi_tangsong_author_make_db(db, shi)
    from src.shi_tangsong import make_db as shi_tangsomg_make_db
    shi_tangsomg_make_db(db, shi)

    shijing = os.path.join(dataPath, 'shijing')
    from src.shijing import make_db as shijing_make_db
    shijing_make_db(db, shijing)


def main():
    args = usage()
    name = args.n
    if name is None:
        print('数据库名称不能为空')
        sys.exit()

    work(name)


if __name__ == "__main__":
    main()
