import os
import argparse

# set up parser
parser = argparse.ArgumentParser(prog='pyinit', description='set up a project folder')

# parent dir
parent = '/Users/archie/repos/'

# create a folder in Users/archie/repos/
parser.add_argument('d', help = 'create a new directory here')

# parse arguments after creating them
args = parser.parse_args()

def main():
    child = parent + args.d # created with args, must come after parsing.

    print(child)

if __name__ == "__main__":
    main()
