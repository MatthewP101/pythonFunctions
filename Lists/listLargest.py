def listLargest(list):
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
    return largest

print("The largest number in the list is:")
list = [5, 10, 15, 20, 789]
print(listLargest(list))