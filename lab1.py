def findDerivativeDescriminant(a , b, c):
  return 4*b*b - 12*a*c

def findFuctionValue(a, b, c, d, x):
    return a*x*x*x + b*x*x + c*x + d

  def findRoot(a, b, c, d, leftValue, rightValue, epsilon):
    btw = (leftValue + rightValue) / 2
    while abs(findFunctionValue(a, b, c, d, btw)) > epsilon:
          if findFunctionValue(a, b, c, d, btw) < -epsilon:
             rightValue = btw
          elif findFunctionValue(a, b, c, d, btw) > epsilon:
             leftValue = btw
          btw = (leftValue + rightValue) / 2
    return btw
  
def findRootInPostiveSide(a, b, c, d, delta, epsilon, leftValue):
     #here i am finding point where function intersects with OX and making inerval to find this point
    while findFunctionValue(a, b, c, d, leftValue + delta) < 0:
          leftValue += delta
    rightValue = leftValue + delta
    root = findRoot(a, b, c, d, leftValue, rightValue, epsilon)
    return root          

def findRootInNegativeSide(a, b, c, d, delta, epsilon, rightValue):
    while findFunctionValue(a, b, c, d, rightValue - delta) > 0:
          rightValue -= delta
    leftValue = rightValue - delta    

    root = findRoot(a, b, c, d, leftValue, rightValue, epsilon)  

    return root  
  
def findingOneRoot(a, b, c, d, epsilon, delta, derivativeDescriminant):
     root = 0
    if derivativeDescriminant != 0:
       if findFunctionValue(a, b, c, d, 0) == 0:
            root = findFunctionValue(a, b, c, d, 0)
       elif findFunctionValue(a, b, c, d, 0) < 0:
            root = findRootInPostiveSide(a, b, c, d, delta, epsilon, 0)
       elif findFunctionValue(a, b, c, d, 0) > 0:
            root = findRootInNegativeSide(a, b, c, d, delta, epsilon, 0)       
       print('Однократный корень: ', root)
    elif derivativeDescriminant == 0: 
         if findFunctionValue(a, b, c, d, 0) == 0:
            root = findFunctionValue(a, b, c, d, 0)
         elif findFunctionValue(a, b, c, d, 0) < 0:
            root = findRootInPostiveSide(a, b, c, d, delta, epsilon, 0)
         elif findFunctionValue(a, b, c, d, 0) < 0:
            root = findRootInNegativeSide(a, b, c, d, delta, epsilon, 0)   
         print('Трёхкратный корень: ', root)     
  

def findingDerivativeRoots(a, b, descriminant):
    root1 = (-2 * b - descriminant ** 0.5) / (6 * a)
    root2 = (-2 * b + descriminant ** 0.5) / (6 * a)

    return root1, root2
  
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
       findingOneRoot(a, b, c, d, epsilon, delta, derivativeDescriminant)
    elif derivativeDescriminant > 0:
       findingTwoOrThreeRoots(a, b, c, d, epsilon, delta)
