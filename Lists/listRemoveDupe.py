def remove_duplicates(items):
    """return a new list with duplicate values removed."""
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

print("The list with duplicates removed is:")
list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
print(remove_duplicates(list))

#items.append(value)
#items.remove(value)
#len(items)

#items[0]     # first item
#items[-1]    # last item
#items[1:4]   # slice