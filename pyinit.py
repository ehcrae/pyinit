import os
import argparse
import template
# set up parser
parser = argparse.ArgumentParser(prog='pyinit', description='create a project folder')

#parser.add_argument('c', type=str, help='create a new directory here')
parser.add_argument('-p', '--parent', type=str, help='change the parent directory') # optional arg last
parser.add_argument('-t', '--template', type=str, help='set the template for the project')

def main():
    args = parser.parse_args() # parse arguments after creating them
    parent = '/Users/archie/repos/'
    
    if args.parent:
        parent = args.parent
    if args.template:
        type = args.template
        for i in template.website:
            print(template.website[i])
    #child = parent+args.c # must come after parse_args

    #print('created '+child)

    #os.mkdir(child)

if __name__ == "__main__":
    main()