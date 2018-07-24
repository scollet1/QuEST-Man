import sys
import json
import yaml
from parser import parse
from pprint import pprint
from random import random, choice

randQuest = ['files', 'comments', 'code']

class Manager():
    def __init__(self, path):
        self.projDict = self.loadFrom(path)
        if not self.projDict:
            sys.exit(-1)
        self.questList = self.loadQuestList()

    def loadFrom(self, path):
        print (path)
        try:
            with open(path, 'r') as file:
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
#        qList = []
#        while len(qList) < len(self.projDict['user']['projects']):
#            print(self.projDict['projects'])
#            for project in self.projDict['user']['projects']:
#                print(project)
#                if random() <= self.projDict['user']['projects'][project]['info']['priority']:
#                    qList.append(project)
#        return qList
        return None

    def pickQuest(self):
#        print(self.questList)
        return choice(self.questList)

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

