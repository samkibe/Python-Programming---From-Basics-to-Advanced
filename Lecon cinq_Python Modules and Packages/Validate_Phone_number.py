#write a progam to help validate a given phone number.

import re

# phone number validation
#s = "+254721-211-330"
s = "254-721-211-330"
c = re.compile("^[+]{1}[0-9]{6}-[0-9]{3}-[0-9]{3}$")
# c = re.compile("(\+254\s)?[0-9]{3}-[0-9]{3}-[0-9]{3}")

#f = re.findall(c,s)
m = re.search(c,s)
if m:
	print(m.group())
else:
	print("Not a valid phone number. Try again!\n")
#print("Phone Number:", f,"\n")
print("Forgive us if it's your 'correct' randomized phone number.\nWe humbly distance ourselves incase of any damages. No offence!!")

