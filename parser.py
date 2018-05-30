import re
import json
import subprocess

def parse():
    parsedData = {}
    subprocess.call(['./cloc-git.sh https://github.com/scollet1/Retrobot.git'], shell=True)
    try:
        with open('out.txt') as file:
            for line in file:
                if 'SUM' in line:
                    x = list(map(int, re.compile('\d+(?:\.\d+)?').findall(line))) # TODO : make pretty
                    parsedData['files'] = x[0]
                    parsedData['comments'] = x[2]
                    parsedData['code'] = x[3]
    except IOError as e:
        print "Unable to open file"
    return parsedData
