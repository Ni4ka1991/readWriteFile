#!/usr/bin/env Python3

from os import system


system( "clear" )

file = open( "in.txt", "r" )

fileContent = file.read()
listContent = fileContent.split()

listNum = []

data = 0

for i in listContent:
    i = int(i)
    listNum.append( i )
    data += i


r = data / len( listContent )
print( f"Result = {r}" )
