# wap to multiply all the items in list
# from functools import reduce

# l = list(range(1,6,1))
# product = reduce(lambda x , y : x * y, l)
# print(product)

l = list(range(1,6,1))
product = 1
for i in l:
    product = product * i
print(product)
