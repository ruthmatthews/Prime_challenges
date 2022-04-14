#challenge 1: list all factors of a number
def factors(n):
    factors = []
    for i in range (1, n+1):
        if n%i == 0:
            factors.append(i)
    return factors

#test challenge 1
print("Factors of 9:")
print(factors(9))

#challenge 2: list the primes up to a number
def primes(n):
    primes = []
    for i in range (1, n+1):
        if len(factors(i)) == 2:
            primes.append(i)
    return primes

#test challenge 2 
print("Primes up to 12:")
print(primes(12))

#challenge 3: list all unique prime factors
def unique_prime_factors(n):
    unique_prime_factors = []
    for i in range (1, n+1):
        if (n%i == 0) and (len(factors(i)) == 2):
            unique_prime_factors.append(i)
    return unique_prime_factors

#test challenge 3
print("Unique prime factors of 60:")
print(unique_prime_factors(60))

#challenge 4: return the sum of a number's unique prime factors
def sum_of_unique_prime_factors(n):
    return sum(unique_prime_factors(n))

#test challenge 4
print("Sum of unique prime factors of 60:")
print(sum_of_unique_prime_factors(60))

#challenge 5: list all prime factors
def prime_factors(n):
    prime_factors = []
    while n > 1:
        for i in range (1, n+1):
            if (len(factors(i)) == 2) and (n%i == 0):
                prime_factors.append(i)
                n = int(n/i)
    return sorted(prime_factors)

#test challenge 5
print("Prime factors of 350:")
print(prime_factors(350))

#challenge 6: return the sum of a numbers prime factors
def prime_factor_sum(n):
    return sum(prime_factors(n))

#test challenge 6
print("Sum of prime factors of 30:")
print(prime_factor_sum(30))

#challenge 7: check if a number is semi prime (the product of two primes)
def semi_prime_checker(n):
    if len(prime_factors(n)) == 2:
        return True 
    else:
        return False

#test challenge 7
print("Is 12 semi prime?")
print(semi_prime_checker(12))
print("Is 22 semi prime?")
print(semi_prime_checker(22))

#chellenge 8: list semi-primes up to n
def semi_primes(n):
    semi_primes=[]
    for i in range (1, n+1):
        if semi_prime_checker(i) == True:
            semi_primes.append(i)
    return semi_primes

#test challenge 8
print("Semi primes up to 10:")
print(semi_primes(10))