import random

target = random.randint(1,100)
# print(target)
while True:
    userinput = input("Guess the number or QUIT")
    if(userinput == "QUIT"):
        break
    userinput = int(userinput)
    if(userinput == target):
        print("SUCCESS")
        break
    elif(userinput < target):
        print("Guess is too small, Guess Bigger number")
    else:
        print("Guess is too big, Guess Smaller number")
    
