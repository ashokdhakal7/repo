# membership operators
# in and not in
# var="Ashok Dhakal"
# a="A"
# b="shok"
# c="dhakal"
# d="al"
# print(a, "in", var, ":", a in var)
# print(b,"in", var, ":", b in var)
# print(c,"in", var, ":", c in var)
# print(d,"in", var, ":", d in var)

# identity operators
# is operator and is not operator
# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=a
# print(a is c)
# print (a is b)

# print ("id(a):",id(a))
# print ("id(b):",id(b))
# print ("id(c):",id(c))

a="ashok dhakal"
b=[1,"ashok"]
c=a
d=b
print(a is c)
print (a is b)
print (d is b)

print ("id(a):",id(a))
print ("id(b):",id(b))
print ("id(c):",id(c))
print ("id(d):",id(d))