a = [5,10,15,20,25,30,35,40]
b = ["Aagney" , 14 ,"PT" ]
c = []
d = "Nottingham"
e = list(d)

a.extend(b)
b.remove(14)
del a
b.reverse()
print(b)
print(b[::-1])
f = [36,2,84,57,4,58,6,7,5,66,67,65]
f.sort(reverse=True)
print(f)

# f.reverse()
# print(f)

g = [  "mango","date" , "banana"]
print(g)
g.sort(key=len)
print(g)