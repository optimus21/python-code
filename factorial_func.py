#finding factorial of given number by function recursion method

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

#print(factorial(10))


while True:
    number=input('Enter your number')
    try:
        number=int(number)
        print('Factorial of',number,'is',factorial(number))
        break
    except:
        print('please enter integer value')
