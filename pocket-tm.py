# Written by Cole Lewis, 2022
import sys
from src.tm import tm

def main():
    if (len(sys.argv) > 2):
        print("Error: too many arguments.\nUsage: python3 pocket-tm.py <description text file path>")
        exit(0)
    elif (len(sys.argv) == 1):
        print("one argument")

    print("pocket-tm")
    while True:
        t = tm()
if __name__=="__main__":
    main()
    


    



        