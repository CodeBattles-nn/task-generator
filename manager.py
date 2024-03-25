import os
import sys
from distutils.dir_util import copy_tree

DESCRIPTION = \
    '''
  TestsGenerator's manager.
  
  Instruction manual:
  
  python3 create [NAME] Create a task name NAME. (without everything)
  python3 create [NAME] -e Create a task named NAME with the generation of examples
  python3 create [NAME] -f Create a task named NAME with metadata
  python3 create [NAME] -e -f Create a task named NAME with metadata and examples
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
