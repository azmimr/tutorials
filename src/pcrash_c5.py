# Exercises from Python Crash Course Book
# Chapter 5: if statements

# 5.1
print("5.1")
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5.2 More tests
print("5.2")
print(car.upper() == 'subaru')

# 5.3 Alient Colors 1
print("5.3")
#alien_color = 'green'
alien_color = 'red'

if alien_color == 'green':
    print("You have earned 5 points!")

# 5.4 Alien Color 2 - ifelse
print("5.4")
if alien_color == 'green':
    print("You have earned 5 points!")
else:
    print("You have earned 10 points!")
    
# 5.5 Alien Color 3 - if elseif else
print("5.5")
if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("You have earned 10 points!")
elif alien_color == 'red':    
    print("You have earned 15 points!")
    
# 5.6 & 5.7 - skip

# 5.8 Hello Admin & 5.9
print("5.8")
unames = ['admin','user1', 'john', 'sam', 'tim']
if unames:
    for uname in unames:
        if uname == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + uname + ", thank you for loggin on.")
else:
    print("We need to add more users!")
    
# 5..9
print("5.9")
unames = []
if unames:
    for uname in unames:
        if uname == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + uname + ", thank you for loggin on.")
else:
    print("We need to add more users!")


