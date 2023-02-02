print("file pointer positions")
f=open("file2.txt","r")#open file  file.txt in read mode
print("the filepointer is at byte:",f.tell())
content=f.read()
print("after filepointer is at byte:",f.tell())
f.close()