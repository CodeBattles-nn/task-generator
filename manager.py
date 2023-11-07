import os
import sys
from distutils.dir_util import copy_tree

DESCRIPTION = \
    '''
    Менеджер TestsGeneratorFramework.
    
    Инструкция:
    
    python3 create [NAME]           Создать задачку с именем NAME. (без всего)
    python3 create [NAME] -e        Создать задачку с именем NAME с генерацией примеров
    python3 create [NAME] -f        Создать задачку с именем NAME с метаданными
    python3 create [NAME] -e -f     Создать задачку с именем NAME с метаданными и примерами
    '''

args = sys.argv[1:]

if len(args) == 0:
    print(DESCRIPTION)
    exit()

command = args[0]
args = args[1:]

if command == "create":
    dir_name = args[0]
    dir_path = f"programms/{dir_name}"
    os.mkdir(dir_path)
    copy_tree("core/samples/main", dir_path)

    if "-e" in args:
        copy_tree("core/samples/examples", dir_path, update=1)

    if "-f" in args:
        copy_tree("core/samples/meta_data", dir_path)
else:
    print(DESCRIPTION)
