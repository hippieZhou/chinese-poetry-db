# 一键生成古诗词数据库文件

## 项目初衷

本项目创建的本质目的是为了让使用任何开发语言的开发者能够将 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) 仓库中的最新数据以最简单
有效的方式进行整合，然后能够快速得到一个可用和可集成的数据库文件。方便开发者快速集成。

## 目前支持的古诗词种类

- 词
- 诗
- 论语
- 诗经
- 四书五经

## 运行环境

python 3.x 即可

## 使用方法

> 为了保证数据能及时更新，请自行先将官方项目克隆到本地，然后将里面的 **ci**、**json** 、**lunyu**、**shijing**、**sishuwujing**、复制到本项目的 **Data** 目录中。

### 支持的数据库类型

#### SQLite

```python
# 创建默认数据库文件 default.sqlite3
python3 manage.py

# 自定义数据库文件名称
python3 manage.py default.db
```

#### MySql

> todo

## 注意事项

由于数据量过大，所以运行时间较长，还请耐心等待！

## 相关参考

- [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
- [chinese-poetry-mysql](https://github.com/KomaBeyond/chinese-poetry-mysql)
