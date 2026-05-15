spam_amount = 0
print(spam_amount)
#Function calls:. print is a Python function that displays the value passed to it on the screen. 

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

#There are a lot of nuances in this code, so let's look at them one by one.

spam_amount = 0

#Variable assignment: Here we create a variable called spam_amount and assign it the value of 0 using =
#which is called the assignment operator.

print(spam_amount)

#Function calls:. print is a Python function that displays the value passed to it on the screen.
#We call functions by putting parentheses after their name, and putting the inputs (or arguments) to the function in those parentheses.

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

#The first line above is a comment. In Python, comments begin with the # symbol.

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam Spam Spam"
print(viking_song)

#The colon (:) at the end of the if line indicates that a new code block is starting. Subsequent lines which are indented are part of that code block.

viking_song = "Spam " * spam_amount
print(viking_song)
#The * operator can be used to multiply two numbers (3 * 3 evaluates to 9), but we can also multiply a string by a number


#Numbers and arithmetic in Python

spam_amount = 0
#we could ask Python how it would describe the type of thing that spam_amount is:
type(spam_amount)
#It's an int - short for integer. There's another sort of number we commonly encounter in Python:
type(19.95)

#A float is a number with a decimal place - very useful for representing things like weights or proportions.
#"True division" is basically what your calculator does:
print(5 / 2)
print(6 / 2)

#The // operator gives us a result that's rounded down to the next integer.
print(5 // 2)
print(6 // 2)




