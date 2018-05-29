import re
import subprocess

subprocess.call(['./cloc-git.sh https://github.com/scollet1/Retrobot.git'], shell=True)
try:
    with open('out.txt') as file:
        for line in file:
            if 'SUM' in line:
                x = list(map(int, re.compile('\d+(?:\.\d+)?').findall(line))) # TODO : make pretty
                print (x)
except IOError as e:
    print "Unable to open file"
