__author__ = 'cesar17'
from HashTable import *
from collections import deque
import itertools
class Cache(object):
    def __init__(self, N):
        self.N = N      #Tamano de cache
        self.M = 32749
        #self.M = 13

    def politicaClock(self, file):
        pageFaults = 0
        clockHand = 0
        location = []
        hashTable = HashTable(self.M)
        i = 0
        while i < self.N:
            location.append(PageTableEntry())
            i += 1

        for line in file:
            line = line.rstrip('\n')
            if location[clockHand].getValidBit() == 1:
                sMH = StringMH(line)
                value = hashTable.getValue(sMH)
                if value is None:
                    pageFaults = pageFaults + 1
                    while location[clockHand].getRefBit() == 1:
                        location[clockHand].setRefBit(0)
                        clockHand = clockHand + 1
                        clockHand = clockHand % self.N
                    key = location[clockHand].getStringMH()
                    hashTable.deleteKey(key)
                    hashTable.putKeyValue(sMH,clockHand)
                    location[clockHand].setStringMH(sMH)
                    location[clockHand].setRefBit(0)
                    clockHand = clockHand + 1
                    clockHand = clockHand % self.N
                else:
                    if location[value].getRefBit() == 1:
                        location[value].setRefBit(0)
                    else:
                        location[value].setRefBit(1)
            else:
                sMH = StringMH(line)
                value = hashTable.getValue(sMH)
                if value is None:
                    pageFaults =  pageFaults + 1
                    hashTable.putKeyValue(sMH,clockHand)
                    location[clockHand].setStringMH(sMH)
                    location[clockHand].setValidBit(1)
                    location[clockHand].setRefBit(0)
                    clockHand = clockHand + 1
                    clockHand = clockHand % self.N
                else:
                    if location[value].getRefBit() == 1:
                        location[value].setRefBit(0)
                    else:
                        location[value].setRefBit(1)
        print "Page Faults:  " + " " + str(pageFaults)