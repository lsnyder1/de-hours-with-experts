#!/usr/bin/python3
import sys
import classes

def main():
    print (next_biggest_number(sys.argv[1]))


def next_biggest_number(num):
    #TODO: Implement me!
    #went a little ham here and used a class. I'm a little rusty with python so I had a little fun with this.
    numberObj=classes.NumberObj(num)
    return numberObj.getNextBiggest()

if __name__ == "__main__":
    main()
