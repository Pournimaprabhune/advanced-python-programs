#open the file.txt in read mode cause error if no such file exits
f=open("file2.txt","r")
#stores alll the data of the file into the varibale content
content=f.read(10)
#prints the type of the data stored in the data
print(type(content))
print(content)
#closes the opened file
f.close()