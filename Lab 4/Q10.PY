#WAP to check if each number is prime in given list of numbers. Print the prime number if any, otherwise print "no prime numbers"

numbers = [1, 2, 3, 77, 98, 137]
prime_found = False
l = []
for number in numbers:
    if number > 1:  
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            l.append(number)
           # print(f"{number} is a prime number")
            prime_found = True

if not prime_found:
    print("No prime numbers")
    
print(l)
