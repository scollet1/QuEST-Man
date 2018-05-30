import sys
import json
from random import random, choice

randQuest = ['files', 'comments', 'code']

class Manager():
    def __init__(self, path):
        self.projDict = self.loadFrom(path)
        if not self.projDict:
            sys.exit(-1)
        self.questList = self.loadQuestList()

    def loadFrom(self, path):
        try:
            with open(path) as file:
                loaded = json.load(file)
                return loaded
        except IOError as e:
            print ("Unable to open file with error: ", e)

    def saveTo(self, path):
        pass

    def loadQuestList(self):
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
