import json
from parser import parse
from manager import Manager

def run():
    man = Manager()
    chosenQuest = man.pickQuest()
    
    print()


if __name__=="__main__":
    run()
