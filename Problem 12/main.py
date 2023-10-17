import time, sympy 

class Primes:
    def __init__(self):
        self.prime_list = []

    def next_prime(self):
        self.prime_list.append(sympy.prime(len(self.prime_list) + 1))

    def get(self, index):
        if index < len(self.prime_list):
            return self.prime_list[index]
        else:
            for i in range(index + 1 - len(self.prime_list)):
                self.next_prime()
            return self.prime_list[index]
        
        

def make_triangle(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum

def old_prime_decomposition(remainder, last_prime = 0, original_prime_list = []):
    prime_list = original_prime_list[:]
    if primes[last_prime] > remainder:
        return prime_list
    elif remainder % primes[last_prime] == 0:
        prime_list.append(primes[last_prime])
        return prime_decomposition(remainder/primes[last_prime], last_prime, prime_list)
    else:
        return prime_decomposition(remainder, last_prime + 1, prime_list)
    
def prime_decomposition(number):
    prime_list = []
    current_prime_index = 0
    current_number = number
    while primes.get(current_prime_index) <= 200:
        if current_number % primes.get(current_prime_index) == 0:
            prime_list.append(primes.get(current_prime_index))
            current_number /= primes.get(current_prime_index)
        elif len(prime_list) == 0 and current_prime_index > 1:
            return([1, number])
        else:
            current_prime_index += 1
    return prime_list
    
def factors_from_primes(original_number, prime_list, original_factors = []):
    factors = original_factors[:]
    if len(factors) == 0:
        factors.append(original_number)
    if len(prime_list) == 0:
        return factors
    
    prime = prime_list[-1]
    prime_used = False
    new_factors = []
    for factor in factors:
        quotient = factor / prime
        if factor % prime == 0 and quotient not in factors:
            factors.append(quotient)
            prime_used = True
    if prime_used:
        return factors_from_primes(original_number,prime_list, factors)
    else:
        return factors_from_primes(original_number,prime_list[:-1], factors)




def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

primes = Primes()

target_divisors = 500

start = time.time()
number = 0
max_divisors = 0
i = 0


while True:
    try:
        i += 1
        number += i
        number_primes = prime_decomposition(number)
        factors = factors_from_primes(number, number_primes)
        # factors = get_factors(number)
        number_of_divisors = len(factors)
        #print(f"Number: {number}, Divisors: {number_of_divisors}, Largest prime: {number_primes[-1]}")
        if number_of_divisors > max_divisors:
            max_divisors = number_of_divisors
            print(f"Number: {number}, Divisors: {number_of_divisors}, Largest prime: {number_primes[-1]}")
        if number_of_divisors >= target_divisors:
            print(f"Number: {number}, Divisors: {number_of_divisors}")
            print(f"Primes: {number_primes}")
            break
        
    except:
        print(f"Error on number: {number}")
        break

end = time.time()

print(f"Time elapsed: {end - start}")





