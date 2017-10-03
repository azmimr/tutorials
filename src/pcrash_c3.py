# Exercises from Python Crash Course Book
# Chapter 3: Introducing Lists

# 3.1 Names - accessing individual elements in a list
names = ['John', 'David', 'Sam', 'Matt']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

# 3.2 Greetings - Personalized
print("Hello " + names[0] + ". How are you?")
# Redo later using a loop

# 3.3 Customized messages - skip

# 3.4 Guest List
print("3.4")
print("Dear " + names[0] + ", your are invited to the party this Sunday.")
print("Dear " + names[1] + ", your are invited to the party this Sunday.")
print("Dear " + names[2] + ", your are invited to the party this Sunday.")
print("Dear " + names[3] + ", your are invited to the party this Sunday.")

# 3.5 Change list
print("3.5")
print(names[1] + " cannot make it to the party.")
names[1] = "James"
print("Dear " + names[0] + ", your are invited to the party this Sunday.")
print("Dear " + names[1] + ", your are invited to the party this Sunday.")
print("Dear " + names[2] + ", your are invited to the party this Sunday.")
print("Dear " + names[3] + ", your are invited to the party this Sunday.")

# 3.6 More Guests
print("3.6")
print("Bigger table found!")
names.insert(0, "Alan")
names.insert(2, "Alvin")
names.append("Jerry")
print("Dear " + names[0] + ", your are invited to the party this Sunday.")
print("Dear " + names[1] + ", your are invited to the party this Sunday.")
print("Dear " + names[2] + ", your are invited to the party this Sunday.")
print("Dear " + names[3] + ", your are invited to the party this Sunday.")
print("Dear " + names[4] + ", your are invited to the party this Sunday.")
print("Dear " + names[5] + ", your are invited to the party this Sunday.")
print("Dear " + names[6] + ", your are invited to the party this Sunday.")

# 3.7 Shrinking Guest List
print("3.7")
print("Table does not arrive in time. Only space for 2!")
uninvite = names.pop()
print("Sorry " + uninvite + ", I can't invite you to dinner.")
uninvite = names.pop()
print("Sorry " + uninvite + ", I can't invite you to dinner.")
uninvite = names.pop()
print("Sorry " + uninvite + ", I can't invite you to dinner.")
uninvite = names.pop()
print("Sorry " + uninvite + ", I can't invite you to dinner.")
uninvite = names.pop()
print("Sorry " + uninvite + ", I can't invite you to dinner.")

print("Dear " + names[0] + ", your are invited to the party this Sunday.")
print("Dear " + names[1] + ", your are invited to the party this Sunday.")

del names[0]
del names[1]
#print("Empty List:" + str(names)) # throws Error due to empty list