def area (length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

pool =area(5, 3)

print ("The area is:")
print (pool[0])  # Print the area

print ("The perimeter is:")
print (pool[1])  # Print the perimeter

/    # normal division
//   # integer division
%    # remainder