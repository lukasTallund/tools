#!/usr/bin/python3
from pykolli import KolliId
import sys
if len(sys.argv)>1:
    myId = KolliId(sys.argv[1])
    print(myId.get_last_update())
else:
    print("Usage: {} kolli-id".format(__file__))
