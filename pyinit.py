import os
import argparse

# set up parser
parser = argparse.ArgumentParser(prog='pyinit', description='create a project folder')

parser.add_argument('c', help='create a new directory here')


parser.add_argument('-p', '--parent', help='change the parent directory') # as this is an optional arg, add it last

# parse arguments after creating them
args = parser.parse_args()

def main():
    parent = '/Users/archie/repos/'
    
    if args.parent:
        parent = args.parent

    child = parent + args.c # must come after parse_args
    
    print('created '+ child)

    os.mkdir(child)

if __name__ == "__main__":
    main()
