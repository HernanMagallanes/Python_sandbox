# Opening Files with Default Applications

import subprocess

# write file
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()

# open file like subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)
