#########################
#
# python file manager
#
# by github.com/ehcrae
#
#########################

import os
import argparse
import template

# set up parser and args
parser = argparse.ArgumentParser(prog='pyinit', description='create a project folder')

parser.add_argument('c', type=str, help='create a new directory here')
parser.add_argument('-t', '--template', type=str, help='set the template for the project')
parser.add_argument('-p', '--parent', type=str, help='change the parent directory') # optional arg last
parser.add_argument('-r', '--readme', type=str, help='create an empty README.md file in the project directory')
args = parser.parse_args()

parent = args.parent if args.parent else '/Users/archie/test/' # if new parent, assign
child = parent+args.c

def template_maker(type):
    for i in template.typedict[type]:
        filepath = os.path.join(child, i)
        open(filepath, 'a')
        print('created '+filepath)

def main():
    print('created '+child)
    os.mkdir(child)

    if args.template: # if template, call maker
        template_maker(str(args.template))
    
    if args.readme:
        readme = child + '/README.md'
        open(readme, 'a')

    print('\ncd '+child+' | code '+child+'\n')
if __name__ == "__main__":
    main()
