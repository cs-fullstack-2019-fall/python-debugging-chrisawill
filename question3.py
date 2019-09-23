# ### Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.

userInput = int(input("Enter a negative number"))
# line 6, in <module> for index in range[7, userInput-1, -1]: TypeError: 'type' object is not subscriptable
for index in range[7, userInput-1, -1]: # you have barckets here instead of parenthesis
    print(index)