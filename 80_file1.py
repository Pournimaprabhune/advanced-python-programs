import subprocess
with open("output.txt","w")as f :
                        subprocess.check_call(["python","79_file.py"],stdout=f)