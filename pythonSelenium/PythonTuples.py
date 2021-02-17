my_tuple = ("Apples", "Oranges", "Grapes")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

my_tuple2 = ("Banana", (1,2,3), ["tokyo", "new delhi"])
print(my_tuple2)
print(my_tuple2[2][1])
print("Banana" in my_tuple2)