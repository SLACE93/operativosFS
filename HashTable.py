__author__ = 'cesar17'
class HashTable(object):

    def __init__(self, M):
        self.M = M          # tamano del HashTable
        self.hashTable = []
        i = 0
        while i < self.M:
            sst = []   # sst lista para manejar las colisiones para un mismo hash
            self.hashTable.append(sst)
            i += 1

    def hash(self, key):
        return (key.hashCode() & 0x7fffffff) % self.M

    def getValue(self, key):
        sst = self.hashTable[self.hash(key)]
        return self.getValueInner(sst,key)

    def getValueInner(self, sst, key):
        if sst:
            for keyvalue in sst:
                keyaux = keyvalue.getKey()
                if key == keyaux:
                    return keyvalue.getValue()
        return None

    def updateValue(self, key, newvalue):
        sst = self.hashTable[self.hash(key)]
        self.updateValueInner(sst, key, newvalue)

    def updateValueInner(self, sst, key, newvalue):
        if sst:
            for keyvalue in sst:
                keyaux = keyvalue.getKey()
                if key == keyaux:
                    keyvalue.setValue(newvalue)
                    break
        #return None

    def deleteKey(self, key):
        sst = self.hashTable[self.hash(key)]
        if sst:
            count = 0
            for keyvalue in sst:
                keyaux = keyvalue.getKey()
                if key == keyaux:
                    return sst.pop(count)
                    #break
                count = count + 1
        return None

    def putKeyValue(self, key, value):
        sst = self.hashTable[self.hash(key)]
        self.putInner(sst, key, value)

    def putInner(self, sst, key, value):
        keyvalue = KeyValue(key, value)
        sst.append(keyvalue)


class KeyValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def setValue(self, newValue):  #Solo para cambiar referencia al indice de la Tabla de pagina
        self.value = newValue


class StringMH(object):
    def __init__(self, string):
        self.string = string
        self.hash = 0

    def hashCode(self):
        h = self.hash
        if h!=0:
            return self.hash
        for c in self.string:
            h = ord(c) + (31 * h)
        self.hash = h
        return h

    def __eq__(self, other):
        if type(other) is type(self):
            return self.string == other.string
        return False