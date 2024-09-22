# wap to print a specified list after removing 0th, 4th, and 5th element.

l = ['red', 'green', 'white', 'black', 'pink', 'yellow']

# l.pop(5)
# l.pop(4)
# l.pop(0)
l.remove('red')
l.remove('black')
l.remove('yellow')

print(l)

#remove() : remove by values
#pop(): removed by index or positions