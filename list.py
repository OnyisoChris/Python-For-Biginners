fruits = ["Mango", "Banana", "Orange",]
print(fruits)
print(fruits[1])
fruits[1] = "Grapes"
print(fruits[1])

lucky_numbers = [7, 17, 27, 37, 47]
fruits.extend(lucky_numbers)
fruits.append("Avocado")
fruits.insert(1, "Guavas")
fruits.remove("Guavas")
#fruits.clear()
fruits.pop() #removes the last element from the list
print(fruits)
print(fruits.index("Mango"))
print(fruits.count("Orange"))
lucky_numbers.sort() #sorts the list is ascending order.
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

fruits2 = fruits.copy()
print(fruits2)