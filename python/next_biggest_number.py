#!/usr/bin/python3
import sys
import classes

def main():
    print (next_biggest_number(sys.argv[1]))


def next_biggest_number(num):
    #TODO: Implement me!
    numberObj=classes.NumberObj(num)

    return numberObj.getNextBiggest()
    #return numberObj.getNextBiggest()
if __name__ == "__main__":
    main()
