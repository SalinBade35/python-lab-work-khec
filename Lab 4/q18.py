# wap to generate and print a list of first and last 5 elements where the values are square numbers between 1 and 15( both included)


l1 = [x**2 for x in range(1, 6, 1)]
l2 = [y**2 for y in range(10, 16, 1)]
print(l1 + l2)
