# for x in range(1,100,2):
# 	y = [x]

x = [1,2,3,4,5,6,7,8,9,10]

def square(k):
	return k**2

def cube(k):
	return k**3

result_1 = map(square, x)
result_2 = map(cube, x)


print("SQUARES")
for i in result_1:
	
	print(i)

print("CUBES")
for i in result_2:

	print(i)
