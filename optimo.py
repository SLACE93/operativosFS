__author__ = 'lejacome'
from HashTable import *
from collections import deque
import itertools
class Cache(object):
    def __init__(self, N):
        self.N = N      #Tamano de cache
        self.M = 32749
        #self.M = 13

		
		
		
 #Implementacion de politica de reemplazo Optimo por ***Luis Jacome***
def politicaOPTIMO(pages,N):
	pages = pages.rstrip('\n')
	pages_in_memory = N   
	op_list = [] 		  
	op_dict = {} 
	compare = 0  
	op_page_fault = 0 
	
	for i in range(len(pages)):
		page = pages[i]	
		
		if len(op_list) < pages_in_memory: 
			page_in_list = Page_Check(op_list, page, len(op_list)) 
			if not(page_in_list):
				op_list.append(page)
				op_page_fault += 1 
		
		else:
			
			page_in_list = Page_Check(op_list, page, pages_in_memory) 
			if not(page_in_list):
				lock_page = 0 
				
				for j in range(pages_in_memory):
					compare = Compare(op_list[j],pages,i) 
					if (compare > lock_page):
						lock_page = compare
					else:
						continue
					op_dict[lock_page] = op_list[j] 
					page_to_be_removed = op_dict.get(lock_page) 
				
				for k in range(pages_in_memory):
					if op_list[k] == page_to_be_removed:
						op_list[k] = page
						op_page_fault += 1 # Page Fault.
						break
	return op_page_fault
			


"""Functions used by the main algorithms"""


# Checuea si la pagina ya ha sido insertada en la lista
def Page_Check(plist, page, pages):
	for i in range(pages):
		page_in_list = plist[i]
		if page_in_list == page:
			return True
	return False

 
# Compara con las paginas a futuro para saber si volvera a ser llamada
def Compare(page_in_list,pages,counter):
	len_of_remaining_page = (len(pages)) - counter
	remaining_pages = counter-1 
	
	for i in range(1,len_of_remaining_page+1):
		index = i + remaining_pages
		page = pages[index] 
		
		if page_in_list == page:
			return i
		
		if (i == len_of_remaining_page):
			return i

"""Call to functions and printing of the amount of page faults generated
by each  algorithm"""

with open(input_file) as f:

		for pages in f:
			pages = pages.rstrip('\n')
			#print pages
			op_page_faults = politicaOPTIMO(pages,600000)


#op_page_faults = politicaOPTIMO(pages,600000)
inicio = time.time()
print'politicaOPTIMO Page Faults: ' + str(op_page_faults) 
fin = time.time()
total = fin - inicio
print "time:"
print total*1000