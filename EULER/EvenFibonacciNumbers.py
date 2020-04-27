def fibo(num):
    if(num<0):
        return
    
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibo(num-1)+fibo(num-2)



maxLimit = 4000000
sum = 0
i =0 
while(True):
    if(fibo(i)<maxLimit):
        if(fibo(i) % 2 == 0):
            sum+=fibo(i)
    else:
        break
    i+=1
    print(sum)

