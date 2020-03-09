#this program calculates how many tiles you will need
#when tiling a wall or floor

length = float (input("enter room length:"))
width = float (input("enter room width:"))

area = length * width
needed = area * 1.05

print ("You need", needed, "tiles in meters squared")
