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

class Parser():

	def parse_TODOs():
		# https://gist.github.com/nickpascucci/1267938
		# TODO parser part 2
		def get_todos(files):
    		"""Create a list of TODO information based on the given files.
		@param files: List of paths to Python source files.
		@return: List of (person, date, file, line, text) tuples corresponding to
		TODO comments in the given sources.
		"""

		comments = []
		for source_filename in files:
			source_file = open(source_filename, "r")
			line_number = 0
			for line in source_file:
				line_number += 1
				line = line.strip()
				if line.startswith("# TODO"):
					elements = line.split(":")
					todo_info = (elements[2],
					elements[1],
					source_filename,
					str(line_number),
					elements[3].strip())
				comments.append(todo_info)
		return comments

	def parse_repo_stats(self):
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
