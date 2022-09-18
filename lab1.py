def findDerivativeDescriminant(a , b, c):
  return 4*b*b - 12*a*c

def main():
    try:
        #reading coeficients for ax^3 + bx^2 +cx + d
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        d = float(input('d = '))
    except:
        print('Bad input!')

    #3ax^2 + 2bx + c
    derivativeDescriminant = findDerivativeDescriminant(a, b, c)   
