#find a number's square root as well as square

import math

for i in range (0, 11, 1):
    x = math.sqrt(i)
    print(f"square root of {i}: {x:.2f}")
    print(f"square of {i}: ", (i**2))