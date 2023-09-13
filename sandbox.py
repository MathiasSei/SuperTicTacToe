#Experimenting to see how lists are stored and modified. 
y = 5

x = y
print(x, y)
y = 6
print(x, y)
z = x
print(x, y, z)


yL = [1, 2, 3]
xL = []

gamestate = list(yL)

xL.append(list(yL))

yL.append(4)

pass