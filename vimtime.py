#!/usr/bin/python

import os
import io

def getHours(time):
    numHours="0"
    if (time.count(":") > 1):
        numHours=time[0]

    return numHours

def getMinutes(time):
    numMins="0"
    if (time.count(":") > 1):
        numMins=time[-5:-4]
    else:
        numMins=time[:-6]
    return numMins
    
def getSeconds(time):
    numSecs="0"
    if (time.count(":") > 1):
        numSecs=time[-2:]
    else:
        numSecs=time[-5:]

    return numSecs

def main():

    time=""

    hour=0
    mins=0
    secs=0
    totHour=0
    totMin=0
    totSec=0

    timefile=open("/home/arrow/vimwatch.txt", "r")

    for line in timefile:
        if (line[0] == "#"):
            continue

        time=line[21:-1]
        hour=float(getHours(time))
        mins=float(getMinutes(time))
        secs=float(getSeconds(time))

        totHour+=int(hour)
        totMin+=int(mins)
        totSec+=int(secs)

    print("Total Time Spent in Vim: " + str(totHour) + ":" + str(totMin) + ":" + str(totSec))

main()
