import string
import random
#makes list to save all alphabet letters, numbers, and special characters to randomize later and save them all together on characters
alphabets = list(string.ascii_letters)
digits = list(string.digits)
specialCharacters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def passwordGenerator() :
    #choose the size of the password
    lenght = int(input("Enter password Lenght: "))
    #choose how many letters, numbers and special characters you want on it 
    alphabetsCount = int(input("Enter how many alphabet count in password: "))
    digitsCount = int(input("Enter how many numbers in passowrd: "))
    specialCharactersCount = int(input("Enter how many special characters on password: "))

    charactersCount = alphabetsCount + digitsCount + specialCharactersCount
    #if you choose more characters than the password lenght you want, give error message and start over
    if charactersCount > lenght:
        print ("Character total count is bigger than the password lenght.")
        return
    
    #makes the password variable, and start saving random values from the letters, numbers and special characters for the password
    password = []

    for i in range (alphabetsCount):
        password.append(random.choice(alphabets))

    for i in range (digitsCount):
        password.append(random.choice(digits))

    for i in range (specialCharactersCount):
        password.append(random.choice(specialCharacters))

    #add random values to the password and randomize them everytime
    if (charactersCount < lenght):
        random.shuffle(characters)
        for i in range (lenght - charactersCount):
                password.append(random.choice(characters))
    #after all of them are added, randomize once again
    random.shuffle(password)
    #print the new password that was made. The code for the function ends here, and its called below to make all of this
    
    print("".join(password))

passwordGenerator()