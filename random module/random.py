import random

#choice a random number from list
randomNumber = random.choice([1,2,3])
print("random number from list using choice :",randomNumber)

#choice a random number from tuple
randomNumber = random.choice((4,5,6))
print("random number from tuple using choice :",randomNumber)

#choice a random number from set
randomNumber = random.choice(list({7,8,9}))
print("random number from set using choice :",randomNumber)

#random integers between the given range
randomNumber = random.randint(10,50)
print("random number between given range using randint :",randomNumber)

#random floats between 0.0 to 1
randomNumber = random.random()
print("random float number between 0 to 1 using random :",randomNumber)

#multiple items from sequences without repeating
randomNumber = random.sample([1, 2, 3, 4, 5],3)
print("random multiple number from list using sample :",randomNumber)

randomNumber = random.sample((11, 12, 13, 14, 15),3)
print("random multiple number from tuple using sample :",randomNumber)

randomNumber = random.sample("Hello",3)
print("random multiple number from string using sample :",randomNumber)

#shuffle a sequence (list)
randomNumber = random.shuffle([1,2,3,4,5,6])
print("shuffle number among list :",randomNumber)

#random floating-point number within a specified range
randomNumber = random.uniform(10,20)
print("random number within range using uniform : ",randomNumber)

#random number within a specified range
randomNumber = random.randrange(10,20)
print("random number with range using randrange: ")

#the same random numbers on every run
random.seed(int(input("Enter a seed number : ")))
randomNumber = random.randint(10,20)
print("seed funcion use for same random output: ", randomNumber)