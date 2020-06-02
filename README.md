# NAME

dist-info - получить информацию об установленном дистрибутиве

# VERSION

0.0.1

# SYNOPSIS

```sh
# Устанавливаваем некий модуль:
pip install pytest
```

```python
from dist_info import dists, metadata, files, modules

# Список всех установленных пакетов:
packages = dists()
# -> ['Brlapi', 'Dumper', ...]

DIST_NAME = 'pytest'

# Получаем каталоги с модулями пакета и путь к метаинформации (может быть )
dist_dir, egg_dir = dist_info_paths(DIST_NAME)
# -> '/home/dart/.local/lib/python3.6/site-packages', 
#    '/home/dart/.local/lib/python3.6/site-packages/pytest-5.4.1.dist-info'

# Получаем файлы
package_files = files(DIST_NAME)
# [ '/home/dart/.local/lib/python3.6/site-packages/../../../bin/py.test',
#   '/home/dart/.local/lib/python3.6/site-packages/../../../bin/pytest', ... ]

# Получаем модули пакета
package_modules = modules(DIST_NAME)
# -> ['_pytest', '_pytest._argcomplete', ...]
```

# DESCRIPTION

Позволяет получить модули установленного пакета, файлы и пути к каталогу с метаинформацией пакета, так и каталогу в котром стоит пакет.

Распознаются dist-info, egg-info и egg-link.

В дистрибутив входит одноимённая утилита:

```sh
Вывести список каталогов с модулями (sys.path):
$ dist -s
$ dist --syspath

Вывести все установленные пакеты:
$ dist-info

Вывести сводную информацию о пакете:
$ dist-info <пакет>

Вывести каталог в котором находятся модули пакета:
$ dist-info <пакет> dist

Вывести путь к файлу или каталогу с метаинформацией:
$ dist-info <пакет> egg

Вывести сокращённую метаинформацию:
$ dist-info <пакет> meta

Вывести файлы:
$ dist-info <пакет> files

Вывести модули:
$ dist-info <пакет> modules
```

# INSTALL

```sh
$ pip install dist-info
```

# REQUIREMENTS

* data-printer

# AUTHOR

Kosmina O. Yaroslav <darviarush@mail.ru>

# LICENSE

MIT License

Copyright (c) 2020 Kosmina O. Yaroslav

