def checkEven(x): #checks even on one integer and using boolean
    if x % 2 == 0:
        return True
    else:
        return False

print(checkEven(4))  



list = [1, 2, 3, 4, 5] #check a list of integers for even or odd

for x in list:
    if checkEven(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")



