import sys
import yaml
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

    def loadFrom(self, path):
	'''load repos'''
	# TODO : USE YAML U DUM DUM
        try:
            with open(path) as file:
                loaded = yaml.load(file)
                return loaded
        except IOError as e:
            print ("Unable to open file with error: ", e)

    def saveTo(self, path):
	'''idk what the fuck this is
	saving repos?????
	what am I saving???????
	'''
	# TODO : save to yaml
        pass

    def loadQuestList(self):
	'''loads the quests into a list to randomly select from'''
	# TODO : load quests from /TODO.md/ file
        while len(self.questList) < len(self.projDict['projects']):
            for project in self.projDict['projects']:
                if random() <= project['info']['priority']:
                    self.questList.append(project)

    def pickQuest(self):
        return choice(self.questList)

    def updatePriority(self, priority):
        pass

    def updateQuest(self, quest):
        if quest['comments']
