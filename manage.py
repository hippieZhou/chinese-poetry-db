import argparse
import sqlite3
import os
import time


VERSION = "VERSION 1.0.0"
DOMAIN = "http://hippiezhou.fun"


def get_parser():
    parser = argparse.ArgumentParser()
    parser.description = 'Create DB File CLI Tools.'
    parser.add_argument('name', metavar="name", type=str, nargs="*",
                        help='set db name, the default name = default.sqlite3.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='version information.')
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    # print(args)
    if args['version']:
        print(VERSION)
        return
    name = 'default.sqlite3'
    if len(args['name']) > 0:
        name = args['name'][0]

    s_time = time.time()
    work(name)
    e_time = time.time()
    print('所有数据导入完毕，总耗时：{0} 秒'.format(e_time-s_time))
    print('数据库位置：{0}'.format(os.path.join(os.getcwd(), name)))


def work(name):
    db = os.path.join(os.getcwd(), name)
    if os.path.exists(db):
        os.remove(db)

    dataPath = os.path.join(os.getcwd(), 'data')

    ci = os.path.join(dataPath, 'ci')
    from src.ci_song_author import make_db as ci_song_author_make_db
    ci_song_author_make_db(db, ci)
    from src.ci_song import make_db as ci_song_data_make_db
    ci_song_data_make_db(db, ci)

    lunyu = os.path.join(dataPath, 'lunyu')
    from src.lunyu import make_db as lunyu_make_db
    lunyu_make_db(db, lunyu)

    shi = os.path.join(dataPath, 'json')
    from src.shi_tangsong_author import make_db as shi_tangsong_author_make_db
    shi_tangsong_author_make_db(db, shi)
    from src.shi_tangsong import make_db as shi_tangsomg_make_db
    shi_tangsomg_make_db(db, shi)

    shijing = os.path.join(dataPath, 'shijing')
    from src.shijing import make_db as shijing_make_db
    shijing_make_db(db, shijing)

    sishuwujing = os.path.join(dataPath, 'sishuwujing')
    from src.sishuwujing import make_db as sishuwujing_make_db
    sishuwujing_make_db(db, sishuwujing)


def main():
    command_line_runner()


if __name__ == "__main__":
    main()
