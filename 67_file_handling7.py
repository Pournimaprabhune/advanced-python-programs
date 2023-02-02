#open the file.txt in read mode cause error if no such file exits
f=open("file2.txt","r")
#running a for loop
for i in f:
         print(i)# i contains each lines of the file
         