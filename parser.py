import re
import sys
import json
import subprocess

def scrape_stdout(cmd):
    '''from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html'''
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
#        print line,
        if line == '' and p.poll() != None:
            break
    return stdout

def parse(project):
    parsedData = {}
    resp = scrape_stdout('./cloc-git.sh ' + project)
#    print ("resp === ", resp)
    try:
        for line in resp:
            print (line)
            if 'SUM' in line:
                x = list(map(int, re.compile('\d+(?:\.\d+)?').findall(line))) # TODO : make pretty
                parsedData['files'] = x[0]
                parsedData['comments'] = x[2]
                parsedData['code'] = x[3]
    except IOError as e:
        print "Unable to open file"
    return parsedData
