__author__ = 'cesar17'
from HashTable import *
from collections import deque
import itertools
from DoubleLinkedList import *

class Cache(object):
    def __init__(self, N):
        self.N = N      #Tamano de cache
        self.M = 13
        # El tamanio de la tabla Hash es seleccionado de acuerdo al numero de entradas ingresado... Y este tamanio seleccionado
        # es primo para disminuir la cantidad de colisiones
        if self.N <= 155:
            self.M = 31
        elif self.N <= 1255:
            self.M = 251
        elif self.N <= 10195:
            self.M = 2039
        elif self.N <= 163745:
            self.M = 65521
        elif self.N <= 655355:
            self.M = 262139
        else:
            self.M = 524287

    #Implementacion de politica de reemplazo CLOCK por ***Cesar San Lucas***
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

    # Implementacion de politica de reemplazo LRU  por ***HERNAN ULLON***
    def politicaLRU(self, file):
        location = DoubleLinkedList()
        pageFaults = 0
        indice = 0
        llena = False
        hashTable = HashTable(self.M)
        totalLineas = 0

        for line in file:
            totalLineas += 1
            line = line.rstrip('\n')
            if llena:
                sMH = StringMH(line)
                value = hashTable.getValue(sMH)
                if value is None:
                    pageFaults = pageFaults + 1
                    firstNodeData = location.removeFirstNode()
                    hashTable.deleteKey(firstNodeData)
                    refNode = location.append(sMH)
                    hashTable.putKeyValue(sMH, refNode)
                else:
                    location.remove(value)
                    refNode = location.append(sMH)
                    hashTable.updateValue(sMH, refNode)
            else:
                sMH = StringMH(line)
                value = hashTable.getValue(sMH)
                if value is None:
                    pageFaults = pageFaults + 1
                    refNode = location.append(sMH)
                    hashTable.putKeyValue(sMH, refNode)
                    indice = indice + 1
                    if indice >= self.N:
                        llena = True
                else:
                    location.remove(value)
                    refNode = location.append(sMH)
                    hashTable.updateValue(sMH, refNode)

        missRate = 100*(float(pageFaults)/totalLineas)
        missWarm = 100*(float(pageFaults - self.N)/(totalLineas-self.N))
        mW = pageFaults - self.N
        print "Evaluando una cache LRU con " + str(self.N) + " entradas"
        print "Resultados:"
        print "Miss rate:               %0.2f" %missRate + "%%  (%d" %pageFaults + " misses out of %d" %totalLineas + " references)"
        print "Miss rate (warm cache):  %0.2f" %missWarm + "%%  (%d" %mW + " misses out of %d" %totalLineas + "-%d" %self.N + " references)"
        #print "Page Faults:  " + " " + str(pageFaults)


class PageTableEntry(object):

    def __init__(self):
        self.stringMH = None
        self.refbit = 0
        self.validbit = 0

    def __eq__(self, other):
        if type(other) is type(self):
            return self.stringMH == other.stringMH
        return False

    def getStringMH(self):
        return self.stringMH

    def getRefBit(self):
        return self.refbit

    def getValidBit(self):
        return self.validbit

    def setStringMH(self, sMH):
        self.stringMH = sMH

    def setRefBit(self, value):
        self.refbit = value

    def setValidBit(self, value):
        self.validbit =  value