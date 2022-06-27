# Python3 program to find first  
# and last digits of a number
import math
# from this import d
  
# Find the first digit
def firstDigit(n) :
      
    # Find total number of digits - 1
    digits = (int)(math.log10(n))
    print (digits)
    print (pow(10, digits))
    # Find first digit
    n = (int)(n / pow(10, digits))
  
    # Return first digit
    return n;
  
# Find the last digit
def lastDigit(n) :
      
    # return the last digit
    return (n % 10)
  
# Driver Code
n = 99;
print(firstDigit(n), end = " ") 
print(lastDigit(n))
  
# This code is contributed by rishabh_jain