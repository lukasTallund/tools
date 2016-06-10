#!/usr/bin/python3
import argparse
import sys

from pykolli import KolliId

def main():
    parser = argparse.ArgumentParser(description='Search for kollid.')
    parser.add_argument('kolliid')
    parser.add_argument('--raw', action='store_true', default=False)
    args = parser.parse_args()

    myId = KolliId(args.kolliid)
    if args.raw:
        myId.print_data()
    else:
        myId.print_formated()

if __name__ == "__main__":
    main()
