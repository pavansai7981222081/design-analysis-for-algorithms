def is_prime(n,divisor=2):
    if n<1:
        return False
    if n==divisor:
        return True
    if n%divisor==0:
        return False
    return is_prime(n,divisor+1)


num=int(input("enter a number to check if it's prime:"))
if is_prime(num):
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
