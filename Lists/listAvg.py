def listAvg(list):
    total = 0
    for num in list:
        total +=num
    return total / len(list)

print("The average of the list is:")
list = [5, 10, 15, 20]
print(listAvg(list))