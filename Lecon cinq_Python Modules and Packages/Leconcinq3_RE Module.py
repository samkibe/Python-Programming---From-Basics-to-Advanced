# Regular Expressions | Regx meta characters
import re

# [a-zA-Z] char a,b,c ... z or A,B,C .. z
# [0-9] digit class 0.1.2 ... 9

s = "ABCDE1234A" #valid pattern prints
#s = "AAAAABCDE1234A" #in the regular expression we will use ^ to regulate this command picking it as a correct expression with extra AAAs in the beginning
#s = "ABCDE1234AAAA" #in the regular expression we will use $ at the end to regulate this command picking it as a correct expression with extra AAAs at the end

r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r,s)
print(l)
 
s1 = "8143456789" #valid pattern prints
#s1 = "88888143456789" #in the regular expression we will use ^ to regulate this command picking it as a correct expression with extra 888s in the beginning
#s1 = "81434567899999" #in the regular expression we will use $ at the end to regulate this command picking it as a correct expression with extra 999s at the end
r1 = re.compile("^[6-9][0-9]{9}$")
l1 = re.findall(r1,s1)
print(l1)

#valid date or not
# dd-mm-yyyy
s2 = "28-11-2024"
r2 = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
l2 = re.findall(r2,s2)
print(l2)

# phone number
s3 = "+254729-811-880"
r3 = re.compile("^[+]{1}[0-9]{6}-[0-9]{3}-[0-9]{3}$")
l3 = re.findall(r3,s3)
print(l3)

m = re.search(r2,s2)
print(m)

m = re.search(r2,s2)
if m:
	print(m.group(3))
	print(m.group("date"))  #so if we search through the group by adding an argument it will select that spaecific group of the date block
else:
	print("Pattern not found")