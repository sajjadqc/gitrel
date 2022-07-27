## Find if a number is prime or not

from tkinter import N
def prime_num(x):
    n = 0
    for i in range(2,x):
        if x%i==0:
            n+=1

        else:
            n 
    
    if n==0:
        return "Prime Number"
    else:
        return "Not a prime Number"

if __name__ == "__main__":

    print(prime_num(37))