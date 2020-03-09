#Ricky Deegan
# info taken from https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#This program takes a positive Float as an input
#and outputs its approx squared root

#create function
def sqrt (x):

    r = x # approx root
    percision = 10 ** (-10)
    while abs (x - r * r) > percision: # reducing the difference in r with percision value
            r = (r + x / r) / 2 # add approx root with original input / r and result / 2 
    return r # output 

x = float(input("Please enter a positive number:")) # input for function 

print("The square root of", x, "is approx.", sqrt(x))    