def reverse(x):
    x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
    
    if  -2147483648 < x <= 2147483647: 
       
        return x 
    else:
        return 0



print(reverse(9010000))