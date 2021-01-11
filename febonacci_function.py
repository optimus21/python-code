#program for febonnaci series by using function recurtion method

def febonaci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return febonaci(n-1)+febonaci(n-2)

#applying above function by using while loop
while True:
    numb1=input('Enter your fibo range')
    try:
        numb1=int(numb1)
        if numb1<0:
            print('please enter positive integer number')
            continue
        else:
            for i in range(0,numb1+1):
                print(i,'=',febonaci(i))
            break
    except:
        print('please enter valid positive integer number')
            
