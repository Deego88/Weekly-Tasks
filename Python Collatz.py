# Richard Deegan
# ask user to input a positive integer
a = int(input("enter positive integer:"))
b = 2

# taking the current value and, if it is even, divides it by 2, While a is not equal 1
while  a != 1:

# if a is even
        if (a % b) == 0:
                a = int(a/b)
                print (a)
                
# but if it is odd, multiply it by 3 and adds
        elif (a % b) != 0:
                a = int((a * 3 ) + 1)
                print (a)
