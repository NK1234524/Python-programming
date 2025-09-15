import random 
dice_roll = random.randint(1,10)
print(f"The dice number is : {dice_roll}")

#pick random element from the list 
fruits = ["Apple","Pineapple","Mango","Banana"]
pick=random.choice(fruits)
print(pick)


#Randomly reshuffles the list
f=[1,2,4,5,9]
random.shuffle(f)
print(f)

#Randomly select unique value from list
l=["A","B","C","D","E"]
print(random.sample(l,1))