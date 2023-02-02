f=open("file3.txt","x")#open file  file.txt in read mode 
print(f)
if f:
    print("file created successfully")

f.close()