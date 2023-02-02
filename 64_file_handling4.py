#open the file.txt in append mode.create a new file if no such file exist
f=open("file2.txt","w")
#appending the content to the file
f.write(''' python is the modern day lanaguge.
        It makes things so simple.
        It is the growing programming. ''')
f.close() #closing the opened the        