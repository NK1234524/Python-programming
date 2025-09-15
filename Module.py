def Calculator(a,b):
    print("---Welcome to Calculator---\n")
    print("1.ADD\n")
    print("2.SUBTRACT\n")
    choice = input("Enter the choice : ")
    if choice == "1":
        print(f"Sum is :{a+b}")
    elif choice == "2":
        print(f"Difference is :{a-b}")
    else:
        print("Wrong choice")

