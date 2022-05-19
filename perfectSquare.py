#Given a positive integer num, write a function which returns True if num is a perfect square else False.
#Follow up: Do not use any built-in library function such as sqrt.

def isPerfectSquare(num):
  square = True
  p = int(num**(1/2))
  if p*p == num:
    return square
  else:
    return False

num1 = 16
num2 = 20
num3 = 9
isPerfectSquare(num2)

################################

#              OR

################################

def isPerfectSquare(num):
  #using binary search
   leftPart = 0
   mainPart = num
   midpoint = 0
   square = True
        
   while leftPart <= mainPart:
            midpoint = (leftPart + mainPart) // 2
            
            #check for the perfect square
            if (midpoint * midpoint == num):
                return square
            elif (midpoint * midpoint < num):
                leftPart = midpoint + 1
            else:
                mainPart = midpoint - 1
                
   return False

num1 = 16
num2 = 20
num3 = 9
isPerfectSquare(num3)