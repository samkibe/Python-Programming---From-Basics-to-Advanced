#1. List comprehension 
l = [100,200,300,400,500]
l1 = [value*value for value in l]
print(l1)
# l1 = []
# for value in l:
# 	l1.append(value*value)

# print(l1)

# look for even numbers
l2 = [10,20,25,30,35]
l3 = [value for value in l2 if value%2 == 0]
print(l3)

# find length of string
l4 =['abc','abcd','abcde','cdefghij']
l5 =[len(value) for value in l4]
print(l5)

l6 = [(value1,value2)for value1 in range(1,5) for value2 in range(100,103)]
print(l6, "\n")

# Single list from a bunch of lists
l7 = [[1,2,3],[4,5,6],[7,8,9]]
l8 = [val2 for value in l7 for val2 in value]
# # l8 = [1,2,3,4,5,6,7,8,9] intended output
# l8 = []
# for value in l7:
# 	for val2 in value:
# 		l8.append(val2)
print(l8)

# even or odd in comprehension
l9 = [100,105,110,115,120]
l10 = ["Even" if value%2==0 else "Odd" for value in l9]
print(l10, "\n")

#2. Disc Comprehension
# Dictionary in comprehension 2:4,3:9,4:16 .. 10:100
d = {x:x**2 for x in range (1,11)}
print(d)

# mappinng e.g 'a':97,'b':98, 'c'=99 ... 'z'=122
d1 = {chr(x):x for x in range (97,123)}
print(d1)

# inevrse value then key
d2 = {value:key for key,value in d1.items()}
print(d2, "\n")


# Functional programming
# map, filter,lambda
def sqr(num1):
	return num1**2

# l2 = [] is defined above

result = list(map(sqr,l2))
print(result)
# for value in result:
# 	print(result)


def add(num1,num2) :
	return num1+num2

	# l = []
	# l2 = [] both as defined above

result = list(map(add,l,l2))
print(result)

def check_num(num1):
	if num1 %2 ==0:
		return True

	else:
		return False
	# l2 = [] as above
result1 = list(filter(check_num,l2))
result2 = list(map(check_num,l2))
print(result1)
print(result2)

# lambda
# l2 = [] defined above
result = list(map(lambda num1:num1**2,l2))
print(result)
# checking even numbers using lambda
result = list(filter(lambda num1:num1%2==0,l2))
print(result)

d3 = {8:50,3:40,2:30,1:20,5:10}
l11a = sorted(d3.items())
l11b = sorted(d3.items(),key=lambda x:x[1])
l11c = dict(sorted(d3.items(),key=lambda x:x[1]))
print(l11a)
print(l11b)
print(l11c, "\n")

#Function Iterators
# Generator functions
def printVal(l12):
	for value in l12:
		yield value
		#print(value)
l12 = [ 10,20,30,40,50]
g = printVal(l12)
print(next(g))
print(next(g),"\n") #etc upto 50  the last value



def fibo():
	first_num = 0
	second_num = 1
	yield second_num
	while(True):
		next_val = first_num + second_num
		yield next_val
		first_num,second_num = second_num,next_val


g = fibo()
#print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for value in range (10):
	print(next(g),"\n")

for value in range (20):
	print(next(g))


l13a = (value * value for value in l12)
l13b = [value * value for value in l12]
print(l13a)
print(l13b)
print(next(l13a))
print(next(l13a),"\n") #upto to 50 the last vlaue


# Iterators and itertools

#l12 = [] defined above
i = iter(l12)
# print(i)
# print(next(i)) #value in index 1
# print(next(i)) #printvalue in index 2 etc
for value in i:
	print(value,"\n")

import itertools

#l12 = [] defined above
l13 = [100,200,300,400,500,]
l14 = [100,200,300,400,500,]

i = itertools.chain(l12,l13,l14)
# print (i)
print(next(i)) #value in index 1
print(next(i),"\n") #value in index 1
# print(next(i)) #printvalue in index 2 etc

for value in i:
	print(value,"\n")

#l12 = [] defined above
count = 0
#for value in itertools.cycle(l12): #or
for value in itertools.repeat(l12):
	if count < 20:
		print(value)
	else:
		break
	count+=1


#l12 = [] defined above
i = iter(l12)
t = itertools.tee(i)
print(t)

for value in t[0]:
	print(value, "\n")

# print(next(i))

# range
count = 0
for value in itertools.count(10,5): #increaments by 5 like in argument
#for value in itertools.count(10): #increaments by default 1
#for value in itertools.count(): #increaments by default 1
	if count > 5: #takes us upto 30 - see for
		break
	else:
		print(value,"\n")
	count+=1

dice = [1,2,3,4,5,6]
print(itertools.permutations(dice,2))
print(list(itertools.permutations(dice,2)))

dice = [1,2,3]
print(itertools.permutations(dice,2))
print(list(itertools.permutations(dice,2)))

print(list(itertools.combinations(dice,2)),"\n")