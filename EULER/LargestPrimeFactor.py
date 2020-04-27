import math

def getPrimeFactors(primeFactors):

    while(primeFactors % 2 == 0):
        if(primeFactors == 2):
            
            print(primeFactors)
            primeFactors = primeFactors/2

    for i in range(3,int(math.sqrt(primeFactors))+1,2):

        while primeFactors % i == 0:
            print(i)
            primeFactors = primeFactors / i
    
    if(primeFactors > 2):
       print(i)

  
print(getPrimeFactors(600851475143))
  
        