import argparse
import os

# set up parser
parser = argparse.ArgumentParser(description='Set up a project folder')
args = parser.parse_args()

# create a folder in Users/archie/repos/
parser.add_argument('cd')


# parent dir
parent = '/Users/archie/repos/'



def main():
    print(parent)


if __name__ == "__main__":
    main()
