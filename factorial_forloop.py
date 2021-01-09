#factorial of given number by using for loop

while True:
    numb=input('Enter your number')
    try:
        numb=int(numb)
        result=1
        if numb<0:
            print('Invalid Number please enter positive number')
            continue
        if numb==0 or numb==1:
            print('factorial of',numb,'is','1')
            break
        else:
            for i in range(1,numb+1):
                result*=i
            print('factorial of',numb,'is',result)
            break
    except:
        print('please enter integer number')
        
