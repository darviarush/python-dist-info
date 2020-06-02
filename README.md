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
from dist_info import dist_info_paths, dist_files, files, modules
from data_printer import p

DIST_NAME = 'pytest'

# Получаем каталоги с модулями пакета и метаинформацией
p(dist_info_paths(DIST_NAME))

# Получаем файлы из SOURCES.txt или RECORD файла в каталоге с метаинформацией
p(dist_files(DIST_NAME))

# Получаем файлы эти же файлы, но с полными путями
p(files(DIST_NAME))

# Получаем модули пакета
p(modules(DIST_NAME))
```

# DESCRIPTION

Позволяет получить модули установленного пакета, файлы и пути к каталогу с метаинформацией пакета, так и каталогу в котром стоит пакет.

`pip` и `` не предоставляют такой информации, либо лажают с пакетом установленным через `pip install -e`.

# INSTALL

```sh
$ pip install dist-info
```

# REQUIREMENTS

* argparse
* data-printer

# AUTHOR

Kosmina O. Yaroslav <darviarush@mail.ru>

# LICENSE

MIT License

Copyright (c) 2020 Kosmina O. Yaroslav

