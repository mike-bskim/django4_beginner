# # Lists
#
# Earlier when discussing strings we introduced the concept of a "sequence" in
# Python. Lists can be thought of the most general version of a "sequence" in
# Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!
#
# In this section we will learn about:
#
#     1.) Creating lists
#     2.) Indexing and Slicing Lists
#     3.) Basic List Methods
#     4.) Nesting Lists
#     5.) Introduction to List Comprehensions
#
# Lists are constructed with brackets [] and commas separating every element in the list.
#
# Let's go ahead and see how we can construct lists!

# Assign a list to an variable named my_list
my_list = [1,2,3]
print(my_list)

# We just created a list of integers, but lists can actually
# hold different object types. For example:

my_list = ['A string',23,100.232,'o']


# Just like strings, the len() function will tell you how
# many items are in the sequence of the list.
len(my_list)


##############################
#### Indexing and Slicing ####
##############################

# Indexing and slicing works just like in strings. Let's make a new list to
# remind ourselves of how this works:
my_list = ['one','two','three',4,5]

# Grab element at index 0
print(my_list[0])

# Grab index 1 and everything past it
print(my_list[1:])

# Grab everything UP TO index 3
print(my_list[:3])

# We can also use + to concatenate lists, just like we did for strings.

print(my_list + ['new item'])

# Note: This doesn't actually change the original list!

print(my_list)

# You would have to reassign the list to make the change permanent.


# Reassign
my_list = my_list + ['add new item permanently']

print(my_list)

# We can also use the * for a duplication method similar to strings:

# Make the list double
print(my_list * 2)

# Again doubling not permanent
print(my_list)


#############################
#### Basic List Methods #####
#############################
#
# If you are familiar with another programming language, you might start to draw
# parallels between arrays in another language and lists in Python. Lists in
# Python however, tend to be more flexible than arrays in other languages for a
# two good reasons: they have no fixed size (meaning we don't have to specify
# how big a list will be), and they have no fixed type constraint (like we've seen above).
#
# Let's go ahead and explore some more special methods for lists:

# Create a new list
mylist = [1,2,3]


# Use the .append() method to permanently add an item to the end of a list:

# Append
mylist.append('append me!')
print(mylist)
 
# Use "pop" to "pop off" an item from the list. By default pop takes off the last
# index, but you can also specify which index to pop off. Let's see an example:

# Pop off the 0 indexed item
mylist.pop(0)
print(mylist)
 
# Assign the popped element, remember default popped index is -1
popped_item = mylist.pop()

print(popped_item)

# Show remaining list
print(mylist)

# It should also be noted that lists indexing will return an error if there is
# no element at that index. For example:
print(len(mylist))
# mylist[100] # return error


# We can use the **sort** method and the **reverse** methods
# to also effect your lists:

new_list = ['a','e','x','b','c']

#Show
print(new_list)

# Use reverse to reverse order (this is permanent!)
new_list.reverse()

print(new_list)

# Use sort to sort the list (in this case alphabetical order,
# but for numbers it will go ascending)
new_list.sort()

print(new_list)

 

# We used list comprehension here to grab the first element of every row in the
# matrix object. We will cover this in much more detail later on!

unsorted_list = [123, 5, 4, 14215, 2, 6, 12467, 1, 923, 991, 42]
unsorted_list.sort()
print(unsorted_list.sort()[:3])
print(unsorted_list)
print(unsorted_list[:3])
