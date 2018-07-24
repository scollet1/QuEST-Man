import json
from parser import parse
from manager import Manager

SAVE_PATH = './Projects.yml'

def generate():
    man = Manager(SAVE_PATH)
    chosenQuest = man.pickQuest()
    man.saveTo(SAVE_PATH)
    return chosenQuest

if __name__=="__main__":
    generate()
