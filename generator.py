import json
from parser import parse
from manager import Manager

SAVE_PATH = './Projects.yml'

def generate():
    man = Manager(SAVE_PATH)
    chosenQuest = man.pickQuest()
    return chosenQuest

if __name__=="__main__":
    print ()
    print ()
    print ()
    print ()
    print ()
    print(generate())
