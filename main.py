import random
def willekeurignummer(): #Making function
    print('Give me 2 numbers, a minimum and a max to generate a random number') #Intro message
    x = int(input("Enter a minimum: ")) #User inputs a minimum
    y = int(input("Enter a maximum: ")) #User inputs a maximum
    z = int(input("How many numbers do you want to generate? ")) #User chooses how much numbers have to be generated
    b = 0 #Starting value of b
    while b < z: #If 0 is less than z, keep generating numbers
     print(random.randint(x, y)) #Printing random number
     b +=1 #adding 1 to b

willekeurignummer() #Using Function


