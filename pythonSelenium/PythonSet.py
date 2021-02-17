my_set = {"chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)

print("Clack" in my_set)

my_set.add("pen")
print(my_set)
my_set.update(["Pencil", "Eraser"])
print(my_set)

len(my_set)

my_set.remove("Pencil")
print(my_set)
my_set.discard("Pen")
print(my_set)