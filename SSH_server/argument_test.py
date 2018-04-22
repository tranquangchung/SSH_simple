# import sys
#
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', sys.argv[0])
#
# from subprocess import Popen, PIPE
# p = Popen(["cd", ".."], stdout=PIPE)
# out, err = p.communicate()
# print(out)
# import subprocess
# a = subprocess.call('cd ..', shell=True)
# print(a

import shutil
import os
shutil.move("username5", "..")

# a = os.path.isfile("username4")
# b = os.path.isdir("username4")
# print('--')

# os.remove() will remove a file.
#
# os.rmdir() will remove an empty directory.
#
# shutil.rmtree() will delete a directory and all its contents.