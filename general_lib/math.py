

# Greatest Common Divisor
def gcd(a, b):
    return (a if b==0 else gcd(b, a%b))


# Least Common Multiple
def lcm(a, b):
    return a/gcd(a,b)*b


print(gcd(2,6))
print(lcm(2,6))
