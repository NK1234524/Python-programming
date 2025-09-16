x=4
try:# to test certain set of code for error
 print(x)
except:# let us to handle the error
 print("Not possible")
else :# Executed when try block does not throw any error
 print("Else executed")
finally:# Executed always does not depend on try-exception-else
 print("Finally completed")

if x<0:
 raise Exception("Sorry all done")