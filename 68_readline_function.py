print("reading lines using readline() function")
#open the file.txt in read mode causes error mo such file exists
f=open("file2.txt","r")
#stores all the data of the file into the variable content
content=f.readline()
content1=f.readline()
content2=f.readlines()#it returns the list of the lines till the end of file(EOF)is reched 
print(content)
print(content1)
print(content2)
f.close()#closes the opened file