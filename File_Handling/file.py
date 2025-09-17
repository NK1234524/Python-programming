with open("demofile.txt") as f :
    print(f.read(5))# by specifying of how much character do we need to print it will print that much.
# Now using with gives us a cushion of not closing the file after opening it.
    print(f.readline())