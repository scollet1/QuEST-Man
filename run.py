import sys
from manager import Manager
from generator import generate

def run():
    generate()

if __name__=="__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '--init' or arg == '-i':
            man = Manager('./Projects.yml')
            man.updateProjs()
    else:
        print(generate())
