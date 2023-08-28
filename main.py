# write your code here
favorite_animals= ["dog", "cat", "monkey", "rabbit"]
print(favorite_animals)
print(f"the second animal in this list is {favorite_animals[1]}")
favorite_animals.remove('monkey')
favorite_animals.append('horse')

for animal in favorite_animals:
    print(f"i love {animal}")

numbers= [1, 2, 3, 4, 5]
numbers_sum= 0
for num in numbers:
    num += numbers_sum
print(numbers_sum)