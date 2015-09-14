__author__ = 'lejacome'
from HashTable import *
from collections import deque
import itertools
class Cache(object):
    def __init__(self, N):
        self.N = N      #Tamano de cache
        self.M = 32749
        #self.M = 13
