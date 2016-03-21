# File gcd.py Implementing the GCD Euclidean algorithm

""" Module gcd: contains two implementations of the Euclid
    greatest common divisor algorithm, gcdr and gcd
"""

def gcdr(a,b):
    """ Euclidean algorithm, recursive version, returns GCD. """
    if b==0:
        return a
    else:
        return gcdr(b,a%b)
        
def gcd(a,b):
    """ Euclidean algorithm, non-recursive version, returns GCD. """
    while b:
        a,b=b,a%b
    return a
    
##########################
if __name__ == "__main__":
    import fib
    
    for i in range(955):
        print i, ' ', gcd(fib.fib(i),fib.fib(i+1))  