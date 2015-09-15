import sys
from Cache import *

def main():
    if len(sys.argv) == 4:
        file = open(sys.argv[1])
        if file:
            if sys.argv[2].lower() == "lru":
                try:
                    cacheSize = int(sys.argv[3])
                    cache = Cache(cacheSize)
                    cache.politicaLRU(file)
                except ValueError:
                    print "Favor ingresar un numero en el parametro cache size"
            elif sys.argv[2].lower() == "clock":
                try:
                    cacheSize = int(sys.argv[3])
                    cache = Cache(cacheSize)
                    cache.politicaClock(file)
                except ValueError:
                    print "Favor ingresar un numero en el parametro cache size"
            else:
                print "Lo ingresado en el parametro <politica> es incorrecto"
        else:
            print "Archivo ingresado en parametro <file> no encontrado"
    else:
        print "Cantidad de parametros incorrectos favor ingresar de la siguiente forma"
        print "python cacheSimulator.py <file> <politica> <cacheSize>"

if __name__ == '__main__':
    main()
