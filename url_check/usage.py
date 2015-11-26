#!/usr/bin/python3
from urlChecker import URLChecker 
url = "https://www.myurl.com"

arguments = {"inputArg1" : "xxxx", "inputArg2" : "yyyy"}
myURL = URLChecker(url, arguments)

print( myURL.get_matching_row("string in page") ) 
