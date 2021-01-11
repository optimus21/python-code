
## febonacci series by using lambda function 
fib=lambda a:a if a<=1 else fib(a-1)+fib(a-2)




number=int(input('Enter you febo range'))
for i in range(0,11):
    print(i,'=',fib(i))
