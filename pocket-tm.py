# Written by Cole Lewis, 2022
import sys
from src.tm import tm
import json

def main():
    if (len(sys.argv) > 2):
        print("Error: too many arguments.\nUsage: python3 pocket-tm.py <description text file path>")
        exit(0)
    elif (len(sys.argv) == 1):
        print("Error: too few arguments.\nUsage: python3 pocket-tm.py <description text file path>")

    print("pocket-tm")
    while True:
        try:
            instr = input()
            t = tm(instr)
        except EOFError:
            break
        
if __name__=="__main__":
    main()
    


    



        