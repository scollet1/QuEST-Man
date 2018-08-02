import sys
import git
import yaml
import shutil
from parser import Parser
from pprint import pprint
from random import random, choice

randQuest = ['files', 'comments', 'code']

class Manager():
    def __init__(self, path):
	'''load repos
	if no repositories:
		fuh koff
	generate a questList to use for the
	lifecycle of the server
	'''
        self.projDict = self.loadFrom(path)
        if not self.projDict:
            sys.exit(-1)
        self.questList = self.loadQuestList()
#        print(self.questList)
#        sys.exit(1)

    def loadFrom(self, path):
        print (path)
	'''load repos'''
	# TODO : USE YAML U DUM DUM
        try:
            with open(path) as file:
                loaded = yaml.load(file)
                return loaded
        except IOError as e:
            print ("Unable to load file with error: ", e)

    def saveTo(self, path):
        try:
            with open(path, 'w') as file:
                yaml.dump(self.projDict, file)
        except IOError as e:
            print ("Unable to save file with error: ", e)

    def loadQuestList(self):
        '''clone repos into dirs
        loads repository list and
        makes a call to parser to
        obtain task information'''
        qList = []
        p = Parser()
        for repo in self.projDict['user']['projects']:
            print(repo)
            try:
                git.Git('./repos/').clone(self.projDict['user']['projects'][repo]['info']['repo'])
                qList.append(p.parse_TODOs('./repos/' + repo))
                shutil.rmtree('./repos/' + repo)
            except Exception as e:
                print (e)
                continue
        return qList
        # pass

    def pickQuest(self):
#        print(self.questList)
	p = None; q = None
	while not p:
		p = choice(self.questList)
	while not q:
		q = choice(p)
        return q

    def updatePriority(self, priority, projectName):
        self.projDict['projects']['projectName']['info']['priority'] = priority

    def updateQuest(self, quest):
        if quest['code'] == 0:
            pass
        quest['code'] += quest['code'] * 0.10

    def updateProjs(self):
        for project in self.projDict['user']['projects']:
            pInfo = self.projDict['user']['projects'][project]['info']
            update = parse(pInfo['repo'])
            print (update)
#            sys.exit(1)
#            pprint(self.projDict['projects'])
            for term, value in update.items():
#                print (pInfo)
                self.projDict['user']['projects'][project]['info']['quest'][term] = update[term]
        self.saveTo('./Projects.json')

