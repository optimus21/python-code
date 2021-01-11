#program of febonacci series by using for loop

number=int(input('Enter you febo range'))
first=0
second=1
count=0
for i in range(0,number+1):
    print(i,'=',count)
    first=second
    second=count
    count=first+second
    
