import random
print("--Your turn--")

while True:
    dice_roll = random.randint(1,6)
    print(dice_roll)
    if(dice_roll==6):        
        print("Roll the dice again")
    else:
        print("--Next players move--")
        break
