import math
from ExternalLibs import primality_test

def op_options():
    print('1. pi to the nth\n2. e to the nth\n3. Fibonacci sequence\n4. Prime factors\n5. Next Prime\n6. Floor Cost')

#A function to stop running the program
def stop_function():
    stop = False
    confirm = input('Would you like to continue? Y/N\n')
    if confirm == 'n' or confirm == 'N':
        stop = True
    return stop

def pi_nth(acc):
    if acc > 64:
        print('System cannot handle anything > 64')
    else:
        print(f'Pi is equal to {math.pi:.{acc}f}')

def e_nth(acc):
    if acc > 64:
        print('System cannot handle an accuracy > 64')
    else:
        print(f'e is equal to {math.e:.{acc}f}')

def fib_nth(acc):
    count = 2
    if acc == 0:
        print(0)
        exit()
    elif acc == 1:
        print(1)
        exit()
    prec_1 = 1
    prec_2 = 0
    while count <= acc:
        result = prec_1 + prec_2
        temp = prec_1
        prec_1 = result
        prec_2 = temp
        count += 1
    print(result)

def prime_factors(n): #Fix this so your prime factors appear neatly. Using a list?
    div = 2
    while div <= int(math.sqrt(n)):
        prime = primality_test(div)
        if prime == True:
            if n%div == 0:
                print(div)
        div += 1

def next_prime(n):
    prime = False
    stop = False
    while stop == False:
        while prime == False:
            n += 1
            prime = primality_test(n)
            if not(prime):
                continue
                
        print(n)
        stop = stop_function()
        if not(stop):
            prime = False

def floor_cost(cost):
    width = float(input('What is the width of the floor?\n'))
    height = float(input('What is the height of the floor?\n'))
    area = width * height
    total = area * cost
    print(f'The tiles will cost ${total}0')

def mortgage_calculator(n):
    pass

def alarm_clock():
    pass

def main():
    # Defining a dictionary to choose an operation from
    print('Choose an operation from below:')
    op_options()
    choice = input('')
    n = int(input('Enter the accuracy you would like:\n')) #Fix this. Your project is way beyond accuracy now.
    operations = {'1': pi_nth, '2': e_nth, '3': fib_nth, '4': prime_factors, '5': next_prime,
                  '6': floor_cost}
    result = operations.get(choice)
    result(n)

if __name__ == '__main__': main()