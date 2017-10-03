# Exercises from Python Crash Course Book
# Chapter 4: Working with Lists

# 4.1 Pizzas
pizzas = ['cheese', 'super', 'singapura']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
    
print("I really like pizza!")

# 4.2 Same type of exercise as above - skipped

# 4.3 Count to 20
for num in range(1,21):
    print(num)
    
# 4.4 1 million    
#for num in range(1,1000001):
#    print(num)

# 4.5 Sum a million
nums = list(range(1,1000001))
print(min(nums))
print(max(nums))
print(sum(nums))

# 4.6 Odd numbers
for num in range(1,20,2):
    print(num)

# 4.7 Threes
print("4.7")
threes = list(range(3,30,3))
for num in threes:
    print(num)
    
# 4.8 Cubes
print("4.8")
nums = []
for num in range(1,11):
    val = num **3
    nums.append(val)

print(nums)

# 4.9 Cubes using list comprehension
print("4.9")
cubes = [value**3 for value in range(1,11)]
print("Cubes:")
print(cubes)

print("4.10")
for num in cubes[0:3]:
    print(num)

for num in cubes[-3:]:
    print(num)

#print("4.11")
# skip

#print("4.12")
# skip

# Buffet
print("4.13")
foods = ('rice', 'kebab', 'soup', 'sushi', 'steak')
for food in foods:
    print(food)
    
