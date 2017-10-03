# Exercises from Python Crash Course Book
# Chapter 6: Dictionaries

# 6.1 Person
print("** 6.1 **")
person = {
    'first_name':'john',
    'last_name':'smith',
    'city':'Singapore',
    }
print(person)

# 6.2 Favorite numbers
print("** 6.2 **")
favorite = {
    'John':1,
    'Adam':7,
    'Steven':4,
    'Richard':2,
    'Greg':6
    }
print(favorite)

# 6.3 Glossary 
print("** 6.3 **")
p_dict = {
    'for':'To iterate through values',
    'dictionary':'To store key/value pairs',
    'if':'Conditional statements',
    }
print('for:' + p_dict['for'] + "\n")
print('if:' + p_dict['if'] + "\n")

# 6.4 Glossary 2
print("** 6.4 **")
for key,value in p_dict.items():
    print(key + ":" + value)

# 6.5 Rivers 
print("\n** 6.5 **")
rivers = {
    'nile': 'egypt',
    'amazon':'brazil',
    'ganges':'india',
    'yangtze':'china',
    }

for river,country in rivers.items():
    print("The "+ river.title()+" runs through "+ country.title()+ ".")

for river in rivers.keys():
    print("The "+ river.title()+" river.")
    
for country in rivers.values():
    print("Country = " + country.title())
    
# 6.6 modified
if 'nile' in rivers.keys():
    print("River found!")
else:
    print("River not found!")    

# skip the rest
# 6. 
#print("\n** 6. **")

# 6. 
#print("** 6. **")

# 6. 
#print("** 6. **")
