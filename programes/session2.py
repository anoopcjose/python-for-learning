thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)
thislist = list(thistuple)
print(thislist)

thislist.insert(2,"orange")
print(thislist)

thistuple = tuple(thislist)
print(thistuple)

thistuple = thistuple + tuple("Pappaya")





thistuple = (1, 2, 3)
# y = ("orange",)
# thistuple += y
# print(thistuple)
thislist = list(thistuple)
print(thislist)

thislist.insert(2,5)
print(thislist)

thistuple = tuple(thislist)
print(thistuple)
