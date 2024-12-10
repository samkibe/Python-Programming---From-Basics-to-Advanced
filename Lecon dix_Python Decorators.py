print("Python decorators\n")

# Takes a function as an argument and returns a function
def deco(func):
	def new_func(val1,val2):
		if type(val1)==type(val2):
			return func(val1,val2)
		else:
			return func(str(val1),str(val2))
	return new_func

@deco
def concat(val1,val2):
	return val1 + val2


result = concat(10,10)
print(result)

result = concat("python","string")
print(result)

result = concat("20","string")


print(result)

# Quiz
# one - une
def a (b,c,d):
	pass #function does nothing

# two - deux 
print(type([1,2])) #<class 'list'>

# three - trois
def func():
	pass
print(type(func())) #<class NoneType'>

# four - quarte

# print(type(lambda:none)) <class 'function'>

# five - cinq

a = [1,2,3, None, [], (),]
print(len(a),"\n") #6

# six - six
d,t = lambda p:p*2, lambda p:p*3
x = 2
x = d(x)
print (x)
x = t(x)
print (x)
x = d(x)
print (x) #24

# seven - sept
a = set([1,1,2,3,3,3,4])
print(len(a)) #4

# eight - huit
class Abc:
	def __init__(self,id):
		self.id,id = id,444

a = Abc(123)
print(a.id) #123


# nine - neuf
a = "snow strom"
print(a[6:8], "\n") #tr or to

# ten - dix
names = ["Kibe", "Kibeish", "Kife", "ish ish"]
print("\n".join(names)) #prints all namess in a list on separate line

