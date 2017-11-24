import subprocess
from subprocess import Popen, PIPE, call, run
import os
import sys


text_value = "asdkljasdkljasrffiaoidscxlzmnflaksdjklasd"
text_value2 = "super user is awesome"
text_value3 = "na-east-region-1"
text_value4 = "text"

# Open the File and Run it and Enter in the Text from the Fields Above
#
# # p = run(['python', 'TestInputFile.py'], stdout=PIPE, stdin=PIPE)
# p = Popen(['python', 'TestInputFile.py'], stdout=PIPE, stdin=PIPE)
# p.stdin.write(text_value2)
#
# p.communicate()[0]
#
# # run_file = Popen('TestInputFile.py', stdin=PIPE) #Note: no sheel=True here
# # run_file.communicate(os.linesep.join([text_value, text_value2, text_value3, text_value4]))


p = Popen(['python.exe', 'TestInputFile.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
out, err = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n'.encode())
print(out)