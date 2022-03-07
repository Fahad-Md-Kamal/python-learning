mylist = ["banana", "cherry", "apple"]

print(mylist)# print the list
print(mylist[0]) # print 1st element of the list
print(mylist[-1]) # print last element of the list
# print(mylist[9]) # print 9th element of the list which will return error

# If item inside a list:
if "apple" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("lemon") # Add items to the last of the list
print(mylist)

mylist.insert(1, "blueberry") # Insert items to a index position.
print(mylist)

item = mylist.pop() # Removes last item.
print(mylist)

item = mylist.pop(0) # Removes index item.
print(mylist)

mylist.remove('cherry') # Removes specific item.
print(mylist)

mylist.reverse() # Reverse list order
print(mylist)

nw_list = mylist.copy() # Copy of mylist
print(nw_list)

nw_list.append("New List Item") # add item to the copied list
print(nw_list)

mylist = [2,3,4,5,1,55,2,22,3]

mylist.sort() # sort the items
print(mylist)

new_list = sorted(mylist)
print(new_list)


