''' Получение информации об установленных пакетах '''

import os
import os.path
import re
import sys


class DistNotFound(Exception):
	pass

# class EggLinkIsBad(DistNotFound):
# 	pass


# def read_egg_link(egg_dir):
# 	with open(egg_dir) as f:
# 		src, dist_dir = f.readlines()
# 		src = src.rstrip("\r\n")

# 		for file_src in os.listdir(src):
# 			if file_src.endswith(".egg-info"):
# 				return src, file_src, dist_dir
# 	raise EggLinkIsBad(egg_dir)


def read_file(egg_dir, files):
	''' Считывает первый попавшийся в виде строк '''

	# if egg_dir.endswith('.egg-link'):
	# 	try:
	# 		src, file_src, dist_dir = read_egg_link(egg_dir)
	# 		egg_dir = os.path.join(src, file_src)
	# 	except EggLinkIsBad:
	# 		print(f"Ошибка: в {egg_dir} нет яйца", file=sys.stderr)

	for i in files:
		path = os.path.join(egg_dir, i) if i != '' else egg_dir
		if os.path.isfile(path):
			with open(path) as f:
				return [ line.rstrip("\r\n") for line in f.readlines() ]
	return []


RE_TWICE = re.compile(r'^([\w\-]+): (.*)')
def metadata(egg_dir):
	x = {}

	for line in read_file(egg_dir, ['', 'METADATA', 'PKG-INFO']):
		m = RE_TWICE.match(line)
		if m:
			x[ m.group(1) ] = m.group(2)
	return x


RE_DIST_EXT = re.compile(r'\.(dist-info|egg-info)$')
def dists():
	''' Список установленных пакетов '''
	
	ret = []
	for syspath in sys.path:
		if os.path.isdir(syspath):
			for file in os.listdir(syspath):
				if RE_DIST_EXT.search(file):
					m = metadata(os.path.join(syspath, file))
					if 'Name' in m:
						ret.append(m['Name'])
					else:
						r, ext = os.path.splitext(file)
						ret.append(r)

	return list(sorted(ret))


def dist_info_paths(dist):
	''' Возвращает путь к информации о пакете и папке с исходниками '''
	re_dist = re.compile(r'^' + dist.replace('-', '[_-]') + r'[-.]')

	for syspath in sys.path:
		if os.path.isdir(syspath):
			for file in os.listdir(syspath):

				if re_dist.match(file):
					path = os.path.join(syspath, file)
					if file.endswith(".dist-info"):
						return syspath, path
					if file.endswith(".egg-info"):
						return syspath, path
					# if file.endswith(".egg-link"):
					# 	src, file_src, dist_dir = read_egg_link(path)
					# 	return(
					# 		os.path.abspath(os.path.join(src, dist_dir)),
					# 		os.path.join(src, file_src), 
					# 	)									
	raise DistNotFound(dist)


RE_DIST_NAME = re.compile(r'^(\w+)')
def get_dist_name(egg_dir):
	m = RE_DIST_NAME.match( os.path.basename(egg_dir) )
	return m.group(1)


def find_link(dist):
	''' Находит ссылку на яйцо '''

	maybe = dist + '.egg-link'

	for syspath in sys.path:
		if os.path.isdir(syspath):
			for s in os.listdir(syspath):
				if s == maybe:
					with open(os.path.join(syspath, s)) as f:
						return [ l.rstrip("\r\n") for l in f.readlines() ] 
	return None


def files(dist):
	''' Файлы с абсолютными путями '''
	dist_dir, egg_dir = dist_info_paths(dist)

	ret = read_file(egg_dir, ['installed-files.txt'])
	if ret:
		ret = [ os.path.abspath(os.path.join(egg_dir, f)) for f in ret ]

	if not ret:
		ret = [ os.path.join(dist_dir, s.split(",")[0]) 
			for s in read_file(egg_dir, ['RECORD']) ]

	if not ret:
		egg_link = find_link(dist)
		if egg_link:
			dist_dir, src_dir = egg_link
			package_dir = os.path.abspath( os.path.join(dist_dir, src_dir) )
			for s in read_file(egg_dir, ['SOURCES.txt']):
				path = os.path.join(package_dir, s)
				ret.append(path)

	if not ret:
		src_dir = os.path.join(dist_dir, get_dist_name(egg_dir))

		for catalog, dirs, files in os.walk(src_dir):
			for i in files:
				path = os.path.join(catalog, i)
				if os.path.isfile(path):
					ret.append(path)

	return list(sorted(ret))


def modules(dist):
	''' Возвращает модули установленного пакета '''
	dist_dir, egg_dir = dist_info_paths(dist)
	ls = files(dist)

	count = len(dist_dir)+1
	ls = [ s[count:] for s in ls if s.startswith(dist_dir) ]

	ls = ( (file[:-12] if file.endswith('/__init__.py') else file[:-3] )
		.replace('/', '.')
			for file in ls if file.endswith(".py") )

	return ls