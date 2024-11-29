print("Lecon deux\n")
print("Conditional Statements and Loops\n")

# #1. Condition statements 
# if [condition]:
# 	statements
# elif [condition]
# else:
# 	statements

n1=100
n2=10
if n1 > n2:
	print("n1 is greater than n2\n")
elif n2 > n1:
	print ("n2 is greater than n1\n")
else:
	print("n1 and n2 are equal\n")

if 1:
	print("Statement in if block\n")
else:
	print("Statement in else block\n")

# #Iterating using For Loop:  for loop, while loop
# iterable datatypes in python str, list, tuple, dict
# for [variable_name] in [iterable datatype]:
# 	statements

i = [10,20,30,40,50]

sum = 0
for value in i:
	sum = sum +value
	print(sum, "\n")
#print(sum)

# range(5) 0 1  2  3 4
# range(10,100) 10 11 12 13 .... 99
# range (10,100,5) 10 15 20 25 30 35 40 45 ... 95 

#for value in range(5):
for value in range(10,100,5):
#for value in range(10,100):
	print (value, "\n")

sum = 0
for value in range(1,21):
	sum = sum +value
print(sum, "\n")

# break
# continue
# enumerate

i = [10,20,30,40,50,60]
#key = 41
key = 50

for value in i:
	if value == key:
		print("Element found")
		break
	else:
		continue
else:
	print("Element not found")
print("Statement after the for loop\n")



i = [10,20,30,40,50,60] #position in array
#key = 41
key = 50

for index,value in enumerate(i):
	#print(index,value)
	if value == key:
		print("Element found at index", index, "\n")
		break
	else:
		continue
		#pass
		#print("Statement after the for loop\n")
else:
	print("Element not found\n")
#print("Statement after the for loop\n")


#Iterating using While loop
#while loo

# while [condition]: #true or false
# 	[statements]
# else:

count = 1
sum = 0

while count <=20:
	sum = sum +count
	count = count +1
print(sum)

#write as program to find numbers divisible by 7 and 5, between 1500 and 2700.

for i in range(1500,2701):
	if i%5==0 and i%7==0:
		print(i)


# Write a program to calculate the sum and average of n integers.

n=10
sum=0

for i in range(1,n+1):
	sum+=i
	avg = sum/n
print("Sum:",sum,"Avg:",avg)

	