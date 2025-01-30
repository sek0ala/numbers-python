import math

def primality_test(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
    
def main():
    n = int(input('Enter a number: '))
    print(primality_test(n))

if __name__ == '__main__': main()
