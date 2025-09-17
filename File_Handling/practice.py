# 'a' is used to append a new content on the file without removing earlier content.
with open("demofile.txt","a") as f:
    f.write("\nNow the new content has been added")
with open("demofile.txt") as f:
    print(f.read())

# 'w' is used to overwrite everything in the file 
with open("demofile.txt","w") as f :
    f.write("\n Hello everyone !")
with open("demofile.txt") as f:
    print(f.read())