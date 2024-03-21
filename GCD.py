def gcd_recursive_factorization(a, b):
    
    if b == 0:
        return a
    
    return gcd_recursive_factorization(b, a % b)
num1 = 100
num2 = 1000
print("GCD of", num1, "and", num2, "using recursive factorization:", gcd_recursive_factorization(num1, num2))
