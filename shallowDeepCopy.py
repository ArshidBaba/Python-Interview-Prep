import copy

li1 = [1, 2, [3, 5], 4]
print("li2 ID: ", id(li1), "Value: ", li1)

# li2 = copy.copy(li1)
li2 = li1
print("li2 ID: ", id(li2), "Value: ", li2)
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)
