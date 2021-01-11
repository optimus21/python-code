##febonacci series by using while loop


n1,n2=0,1
count=0
dt=0
while count<=10:
    print(count,'=',dt)
    n1=n2
    n2=dt
    dt=n1+n2
    count+=1
