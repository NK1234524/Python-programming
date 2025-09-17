try:
 f=open("demofile.txt")
except:
 print("Not exist")
else:
 print("File exist")
 print(f.read())
finally:
 print("Code executed successfully")

