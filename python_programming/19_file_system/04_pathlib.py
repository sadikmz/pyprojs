# import os
# import glob
# import shutil
#
#
# for file_name in glob.glob("*.py"):
#     new_path = os.path.join("archive", file_name)
#     shutil.copy(file_name, new_path)
#

import pathlib


print(pathlib.Path.cwd())
print(pathlib.Path.home())
print(pathlib.Path.cwd().parent)
print(pathlib.Path.touch())