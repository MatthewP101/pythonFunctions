x = 5
y = 10
z = 15

def findLargest(x, y, z): #finds the largest of three integers
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


print("The largest number is:")
print(findLargest(x, y, z))


list = [1, 2, 3, 4, 73] #finds the largest number in a list of integers
def LargestList(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest
print("The largest number in the list is:")
print(LargestList(list))





#auto function for highest number in a list
print("Auto Max function:")
print(max(list))
print(max(x, y, z))