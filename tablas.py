
booleanos = [False, True]

# Tabla de verdad de or
for x in booleanos:
        for y in booleanos:
                print(x, y, x or y)

print ()

# Tabla de verdad de and

for x in booleanos:
        for y in booleanos:
                print(x, y, x and y)

print()

#Tabla de verdad de not

for x in booleanos:
	for y in booleanos:
        	print(x, not x) 
print()



