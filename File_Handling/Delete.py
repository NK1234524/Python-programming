import os
#enter the file name required to delete
# to check the file do exist or not
if os.path.exists("Demo.txt"):
    os.remove("Demo.txt")
else:
    print("Do not exist ")

# to remove the directory(Only empty folders) 
os.rmdir("folder name")