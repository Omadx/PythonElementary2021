#list
my_list = ["Tokyo", "london", "New York"]
print(my_list)
print(my_list[2])

for val in my_list:
    print(val)

print(len(my_list))

my_list.append("Boston")
print(my_list)

my_list.insert(4, "lima")
print(my_list)

my_list.remove(("Tokyo"))
print(my_list)

my_list.pop()
print(my_list)