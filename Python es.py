#Richard Deegan
#This program reads in a text file and outputs the number of e's it contains.
x = str("e")

with open ("es.py moby-dick.txt", "r") as myfile:
    data = myfile.read().replace('\n', '') #create data variable to be searched, each line
    print(data)
    freq = 0
    for char in data: #creates a for loop, 
        if char == x: #conditional statement if character is equal to x variable (e)
            freq = freq + 1 #add one ot the freq of occurence 
    print(freq)


# References 
# https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python
# 
