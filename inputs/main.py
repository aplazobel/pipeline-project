import os 
import sys
from argparse import ArgumentParser
from functions import ShowCharacterData


def main():
    parser = ArgumentParser(description="This program shows the death year, GoT book where the character dies, date of death gender and allegiances for all characters in the Game of Thrones universe. If I believe the character is worthy I will even give you the actor's name")
    parser.add_argument("-n","--nombre",help="flag: Please enter the character's name between quotes to retrieve the information. For example: 'Jon Snow' ",default=None)
    
    args = parser.parse_args()
    #print(args)

    if args.nombre:
        nombre=args.nombre
    else:
        nombre=False



    print(ShowCharacterData(args.nombre))

if __name__ == "__main__":
    main()