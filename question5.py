# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.
# line 5 for index of range(len(squad)-1, -1, -1): SyntaxError: invalid syntax
#                    ^
squad = ["One", "Two", "Three", "Four", "Five"]
for index of range(len(squad)-1, -1, -1): #index in range not of range
    print(squad(index))