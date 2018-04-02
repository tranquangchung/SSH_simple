# import sys
#
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', sys.argv[0])

from subprocess import Popen, PIPE
print('---')
p = Popen(["ls", "-la"], stdout=PIPE)
out, err = p.communicate()
print(out.decode("UTF-8"))
print('---')
