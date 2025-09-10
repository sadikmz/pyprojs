import os
from distutils.command.check import check

# os.path.join

path = os.path.join(os.getcwd(), '00_fs.py')
abs_path = os.path.abspath('../../../test.txt')
rel_path= os.path.relpath('../../../test.txt')
# print(path)
print(abs_path)
# print(os.path.isabs(abs_path))
# print(rel_path)
# print(os.sep)

# os.path.dirname()
dir_name = os.path.dirname(abs_path)
base_name = os.path.basename(abs_path)
print(dir_name)
print(base_name)

# os.path.exists()

check_dir = os.path.exists(abs_path)
print(check_dir)
# check_file = os.path.isfile(abs_path)
