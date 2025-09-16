import random
number = random.randint(1,10)
while True:
    guess = int(input("Guess me : \n"))
    if (guess==number):
        print("Correct Match\n")
        print("--Congrats--")
        break
    else:
        print("Wrong guess\n")
        print("Choose again")
        continue