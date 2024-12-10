print("OOP")
# Introducion to Object Oriented Programming
# how to create Classes
# Objects

# how to define instances variables as below
# cust id
# name 
# balance
# deposit
# withdraw

class Account:
	def __init__(self,cust_id,name, initial_bal=0):
	#function explicit
	#self is the object instance
		# self.id = cust_id
		# self.name = name
		# self.balance = initial_bal


	#instance variable as private we use underscores, TO RESTRICT ACCESS OUTSIDE CLASS
		self.__id = cust_id
		self.__name = name
		self.__balance = initial_bal #not accessible outside class because it is now private by use of underscore (__id)

	def get_balance(self):
		return self.__balance

	def get_id(self):
		return self.__id

	def get_name(self):
		return self.__name

	def deposit(self,ammount):
		# self.balance = self.balance + ammount
		self.__balance += ammount
		return self.__balance

	def withdraw(self,ammount):
		if ammount > self.__balance:
			print("Insufficient balance","\n")
		else:
			self.__balance -= ammount
			return self.__balance


customer1 = Account("101","Mwangi")
# Account(customer1,"101","Mwangi")
# print(customer1)
#print(customer1.deposit(5000))
customer1.deposit(5000)
print(customer1.get_balance())
customer1.withdraw(6000)
print(customer1.__dict__)
print(customer1._Account__id, "\n") #how to access a class variable outside its class using undescores

customer2 = Account("102", "Kibet")
#print(customer2)
customer3 = Account("103", "Nafula")
#print(customer1)
customer4 = Account("104", "Saitoti")
#print(customer3)

customer2.deposit(10000)
customer3.deposit(20000)
customer4.deposit(3000)


# print(customer1.id,customer1.name,customer1.balance) #dispalys customer
print(customer1.get_balance()) #gets balance

l = [customer1,customer2,customer3,customer4]

for obj in l:
	if obj.get_balance() < 10000:
		print(obj.get_id(),obj.get_name(), "\n")

#Class Variables 
#Class methods
#Static Methods.


class Account:
	count = 0
	#class method
	@classmethod
	def incr_count(cls):
		cls.count +=1

	@classmethod
	def get_count(cls):
		return cls.count

	#static method
	@staticmethod
	def print_Val():
		print("Static method in account class", "\n")

	def __init__(self,cust_id,name, initial_bal=0): #instance method
		self.__id = cust_id
		self.__name = name
		self.__balance = initial_bal 
		#Account.count += 1
		Account.incr_count()

	def get_balance(self):
		return self.__balance

	def get_id(self):
		return self.__id

	def get_name(self):
		return self.__name

	def deposit(self,ammount):
		self.__balance += ammount
		return self.__balance

	def withdraw(self,ammount):
		if ammount > self.__balance:
			print("Insufficient balance") 
		else:
			self.__balance -= ammount
			return self.__balance


customer1 = Account("101","Mwangi")

# customer1.deposit(5000)
# print(customer.get_balance())
# # customer1.withdraw(2000)

customer2 = Account("102", "Kibet")
customer3 = Account("103", "Nafula")
customer4 = Account("104", "Saitoti")


customer2.deposit(10000)
customer3.deposit(20000)
customer4.deposit(3000)

print(Account.count)
print(Account.get_count())

Account.print_Val()

# INHERITANCE reuse existing code

class Saving_Account(Account):
	def __init__(self,idn,name,initial_bal=0):
		super().__init__(id,name,initial_bal)
		self.limit = 50000

	def withdraw(self,ammount):
		if ammount < self.limit:
			new_bal = super().withdraw(ammount)
			self.limit -= ammount
			return new_bal
		else:
			print("Daily limit reached")


cust1 = Saving_Account(100, "sam")
print(cust1)
print(cust1.__dict__)
print(cust1.deposit(80000)) #finds this method from mother class
print(cust1.withdraw(40000))
print(cust1.withdraw(40000), "\n")

# Multiple inheritance
# A B
# C
class A:
	pass
class B:
	pass
class C(A,B): #Class told to inherit from A TO B
	pass
obj = C()
help(obj)




