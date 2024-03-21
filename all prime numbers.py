def is_prime(n, i=2):
    if n <= 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

user_input = int(input("Enter a number: "))
prime_numbers = generate_primes(user_input)
print("Prime numbers up to", user_input, "are:", prime_numbers)
