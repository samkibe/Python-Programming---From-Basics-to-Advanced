# r => read, strat, file should exist, read
# r+ = read and write, start, file should already exist
# w => write, start, creats a new file, write
# w+ = write and read, deletes something if you use it without update , creates new file
# a =>append, end, craetes a new file, writes at the end
# a+, end cretaes a new file, write and read.

# r = read

fp = open("sam.txt","r")
# # content = fp.read() #reads entire file
# # print(content) 

content = fp.read(100) #argument 100 reads first x=100 characters or words
print(type(content)) 
print(content, "\n")

# content = fp.readlines()
# print(type(content))
# print(content[:5], "\n")

# # reads one line
# content = fp.readline()  # reads one line
# print(content, "\n,\n")

# content = fp.readline()  # reads next line
# print(content)

# content = fp.readline()  # reads next line
# print(content)

for x in fp:
	print(x)

# w = write
# w+ = write and read

# fp = open ("sam1.txt","w")
# fp.write("Write this line to a file sam!")

fp = open ("sam1.txt","w+")
print(fp.tell())
fp.write("Felicitation!") #another line flashes entire file when we use write caution!! and no read mode
print(fp.tell())
content = fp.read() #reads entire file
print(fp.tell())
print(content) 

# tell - current file pointer(fp) position
# seek (offset(number of char),position(start of file))- try to change the fp position
# 1 = current position
# 2 = end of file

# w+ = write and read

fp = open ("samuel.txt","w+") #this create a new file = w+
print(fp.tell())
fp.write("Felicitation!") #another line flashes entire file when we use write caution!! and no read mode
print(fp.tell())
fp.seek(0,0) #this displays result
print(fp.tell())
content = fp.read() #reads entire file
print(fp.tell())
print(content, "\n") 


# r+ read and write

fp = open("sam.txt","r+")
content = fp.read() 
print(content,"\n") 
# fp.write("\n\nSample line added using Python script")

# a = append
# a+ = write at the end of operation

fp = open("sam.txt","a+") 
#print(fp.tell())
fp.write("\n\n abcdefghijklmnopqrstuvwxyz")

# content = fp.read() 
# print(content) 


# JSON PROCESSING
# PARSING json files which include dict {"key":"value"},numbers(int,float), array,tuple
# i did not convert to dictionary
import json

handle = open("sam1.json","r")
content = handle.read()
print(content)

d = json.loads(content)
print(d,"\n")
print(d['personal_info'])
print(d['personal_info']['name'],"\n")

# XML PROCESSING
# PARSING XML FILE USING XMLTODICT

import xmltodict

handle = open("sam1.xml","r")
content = handle.read()
print(content)

# To dict
d1 = xmltodict.parse(content)
print(d1,"\n")

x = xmltodict.unparse(d1)
print(x)



