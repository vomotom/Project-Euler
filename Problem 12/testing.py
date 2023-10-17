import sympy

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
        
    

primes = Primes()

print(primes.get(0))
print(primes.get(1))
print(primes.get(10))
print(primes.prime_list)