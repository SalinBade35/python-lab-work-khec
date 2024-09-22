#wap to sort a list of lists by a given index of the inner list.

l1= [[2,3,1], [1,70,1.2], [4,31,23]]

print("""l1= [[2,3,1], [1,70,1.2], [4,31,23], [1,2,7,6]]\n """)
n = int(input("Entre based on which index  you want to sort:\n1. first\n2. second\n3. third\n "))

# l2 = sorted(l1[n-1])   
# print(l2)
l3 = []
for i in range(0, len(l1)):
    l3.append(l1[i][n-1])
l3.sort()



for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if(l1[i][j] > l1[i][j]):
            l1[i], l1[j] = l1[j], l1[i] 
            
            
print(l1)  


