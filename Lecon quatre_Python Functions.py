#User Defined Functions
#for code reuse
#for Modularity
 
s = "Python", "HTML", "CSS"
print(s.index("CSS"))

#reverse func call, func def

def value_reverse(value):
	if type(value)==list or type(value)==str: #added to also reverse int in a list
		reverse = value[::-1]
	else:
 		temp = str(value)
 		reverse = temp[::-1]
	#print(reverse)
	return reverse

s = "Python"
result = value_reverse(s)
print(result)

l = [100,200,300,400, 500]
result = value_reverse(l)
print(result)

num = 100
result = value_reverse(num)
print(result)

#parameter passing techniques
# passing values to a function

#1. position argument
def linear_search(L,key):
	for value in l:
		if key==value:
			return True
	else:
		return False


key = 400
result = linear_search(l,key)
print(result, "\n")

#2. Default argument system to create a unique password
# 8 chasr pssd
# 1 upper letter
# 1 lower 
# 1 special chasr5 digits

print(ord('a'), ord('z'))
print(ord('A'), ord('Z'))

print(chr(97), "\n")

import random
def gen_password(Length=8): #(Length=8) default =8
	l = ['@','#','$','&']
	upper = chr(random.randint(65,90))
	lower = chr(random.randint(97,122))
	special = random.choice(l)
	digit = random.randint(10000,99999)
	password = upper + lower + special + str(digit)
	l = random.sample(password,Length)
	#print(l)
	password = ("").join(l)
	return password

result = gen_password(4) #if we include an argument >=8 it will generate pswd equal to that argument
print(result)


#3. Keyword argument

def validate(username,password):
	if username == "ABC" and password == "Abc@123":
		print("Valid Password\n")
	else:
		print("Invalid Password\n")

validate("ABC", "Abc@123")
validate("Abc@123","ABC") # ORDER of item will ppass an invalid
validate(password="Abc@123", username = "ABC")

# help(print)
print(100,200, sep=",", end=" ") # this will print both prints in a single line
print("Hi\n")

#VARIABLE LENGHT positional arguments(args)

def add_value(*args):
	#print(args)
	l = []
	for value in args:
		l.append(value)

	return l

result = add_value(100,200,300,400,500)
print(result)
result = add_value(100,200)

result = add_value(100,200,300,400,500,600,700,800)
print(result,"\n")

#5. Variable length keyword args
# name,email,contact,dob

def get_details(**kwargs):
	print(kwargs, "\n")

get_details(name="ABC",email="abc@gmail.com",contact=729811880,dob = "27-8-1989")

get_details(name="ABC",email="abc@gmail.com",dob = "27-8-1989")
get_details(name="ABC",contact=729811880,dob = "27-8-1989")


# RECURSIVE FUCTION - if a function uses a call to itself

# factoria;(5)= 5 * fact(4)
# 					4 * fact(3)
# 						3 * fact(2)
# 							2 * fact(1)

def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num -1)

num1 = 5
result = factorial(num1)
print(result)

#how it works

# factoria;(5)= 5 * 24 = 120
# 					4 * 6 = 24
# 						3 * 2 = 6
# 							2 * 1 = 2
#								1

# Binary searh

def binary_search(l,key):
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


l = [100,200,300,400,500,600,700,800,900]
key = 70000
# mid = 9 / 2= 4 500 == 700 = True
result =binary_search(l,key)
print(result)