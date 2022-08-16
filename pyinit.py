import os
import argparse
import template
# set up parser and args
parser = argparse.ArgumentParser(prog='pyinit', description='create a project folder')

parser.add_argument('c', type=str, help='create a new directory here')
parser.add_argument('-p', '--parent', type=str, help='change the parent directory') # optional arg last
parser.add_argument('-t', '--template', type=str, help='set the template for the project')
args = parser.parse_args()

def template_maker(type):
    for i in template.typedict[type]:
        open(i, 'a')
        print('created ' + i)

def main():

    parent = args.parent if args.parent else '/Users/archie/repos/' # if new parent, assign
    child = parent+args.c
    if args.template: # if template, call maker
        template_maker(str(args.template))

    print('created '+child)
    os.mkdir(child)

if __name__ == "__main__":
    main()