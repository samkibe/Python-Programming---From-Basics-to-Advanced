"""

Docstring: this module contains binary search implementation
Author:Kibe

"""

# Creating Modules and packages

# Binary searh

def binary_search(l,key):

	"""
	Binary search : Inpu a list and key
	return True if key exists else return false
	"""
	if len(l) == 0:
		return False
	else:
		mid = len(l) // 2 #//float operator

		if l[mid] == key:
			return True


		elif key < l[mid]: #elif used to ccheck multiple conditions
			return binary_search(l[:mid],key) #Items on lefthand side

		else:
			return binary_search(l[mid+1:],key)

#print(__name__)

if __name__ =='__main__':
	l = [100,200,300,400,500,600,700,800,900]
	key = 700
	# mid = 9 / 2= 4 500 == 700 = True
	result =binary_search(l,key)
	print(result)