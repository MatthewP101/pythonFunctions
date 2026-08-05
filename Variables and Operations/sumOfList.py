list = [1,]

def appendList(list, value):
  list.append(value)
  return list


appendList(list, 115)


def sumOf(list):
  total = 0
  for i in list:
    total += i
  return total

print("The sum is:")
print(sumOf(list))

