# Exercises from Python Crash Course Book
# Chapter 2: Variables and  Simple Data Types

# STRINGS
# 2.1 Simple message
msg = "Hello World!"
print(msg)

# 2.2 Reuse the variable
msg = "Hello Again!"
print(msg)

# 2.3 Personal Message
nme = "john"
print("Hello " + nme.capitalize() + ", would you like to learn Python today")

# 2.4 Different Cases
print(nme.upper() + " " + nme.lower() + " " + nme.title())

# 2.5 & 2.6 Quotation
quote = "To be or not to be, that is the question."
author = "William Shakespeare"
print(author + ' once said, "'+ quote + '"')

# 2.7 Stripe whitespace
nme = "\tJohn Smith\n "
print("Original:" + nme)
print("L Strip:" + nme.lstrip())
print("R Strip:" + nme.rstrip())
print("Strip:" + nme.strip())

# NUMBERS
# 2.8 Operations
print(5+3) # Addition
print(11-3) # Subtraction
print(2*4) # Multiplication
print(24/3) # Division

# 2.9 Cast number as string
print("My favorite number is " + str(7))

# COMMENTS
# 2.10 Comments - Already done

# 2.11 Zen of Python
import this

