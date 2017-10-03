# Exercises from Python Crash Course Book
# Chapter 7: User Input & While loops

# 7. 2 Restaurant seating
print("\n** 7.2 **")
#===============================================================================
# message = "Welcome to ABC Restaurant."
# message += "\nHow many people are in your party tonight?: "
# size = input(message)
# if int(size) > 8 :
#     print("Please wait for the next avaiable table.")
# else :
#     print("Your table is ready.")
#===============================================================================

# 7.5 Movie Tickets 
print("\n** 7.5 **")
#===============================================================================
# print("Welcome to ABC Movie Theater.")
# print("Please enter your age (type 'quit' to exit.")
# 
# flag = True
# while flag:
#     print(flag)
#     utext = input(">")
#     
#     age = 99 # Default price
#     
#     if utext == 'quit':
#         break
#     else:
#         age = int(utext)
#     
#     if age < 3:
#         print("Your ticket is free!")
#     elif age >= 3 and age < 12:
#         print("The ticket is $10")
#     elif age >= 12:
#         print("The ticket is $15")
#     
# print("Thank you. Goodbye!")        
#===============================================================================
        
# 7.10 Dream Vacation
print("\n** 7.10 **")

poll = {} # empty dictionary
active = True

while active:
    name = input("What is your name? >")
    destination = input("What is your favorite location? >")
    
    poll[name] = destination
    

    cont = input("Would you like to continue(yes/no)?>")
    if cont == 'no':
        active = False

print("Results")
for key, value in poll.items():
    print(key.title() +":"+value.title())

# 7. 
#print("\n** 7. **")