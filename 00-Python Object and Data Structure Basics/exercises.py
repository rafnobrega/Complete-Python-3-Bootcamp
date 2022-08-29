result = 100/777
print("The result was {r:1.3f}".format(r=result))


# Formatted String Literal (f-string)
name = "Jose"
print(f"Hello, his name is {name}")


########### LISTS:
my_list = [1,2,3]

len(my_list)

my_list.pop(2) # remove last item
my_list.append("Hello") # add item to the end
print(my_list)

new_list = ["a", "e", "x", "b", "c"]
new_list.sort() # sort list in alphabetical order
print(new_list)