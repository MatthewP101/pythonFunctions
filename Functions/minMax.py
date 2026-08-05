def minMAX(list):

    if len(list) == 0:
        return None, None
    return min(list), max(list)

print("The minimum and maximum values in the list are:")
list = [5, 10, 15, 20, 789]
min_val, max_val = minMAX(list)
print(f"Minimum: {min_val}, Maximum: {max_val}")