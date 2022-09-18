def findDerivativeDescriminant(a , b, c):
  return 4*b*b - 12*a*c

def findFuctionValue(a, b, c, d, x):
    return a*x*x*x + b*x*x + c*x + d

def findRootInPostiveSide(a, b, c, d, delta, epsilon, leftValue):
    #here i am finding point where function intersects with OX and making inerval to find this point
    while findFuctionValue(a, b, c, d, leftValue + delta) < 0:
          leftValue += delta
    rightValue = leftValue + delta
    
def findingOneRoot(a, b, c, d, epsilon, delta):
    if findFuctionValue(a, b, c, d, 0) == epsilon:
       return findFuctionValue(a, b, c, d, 0)

    elif findFuctionValue(a, b, c, d, 0) > 0:
       return findRootInPostiveSide(a, b, c, d, delta, epsilon, 0)    

    return 
  

def findingTwoOrThreeRoots(a, b, c, d, epsilon, delta):

  return 
  
def main():
    try:
        #reading coeficients for ax^3 + bx^2 +cx + d
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        d = float(input('d = '))
        epsilon = float(input('epsilon = '))
        delta = float(input('delta = '))
    except:
        print('Bad input!')

    #3ax^2 + 2bx + c
    derivativeDescriminant = findDerivativeDescriminant(a, b, c)   

    if derivativeDescriminant <= 0:
       findingOneRoot(a, b, c, d, epsilon, delta)

