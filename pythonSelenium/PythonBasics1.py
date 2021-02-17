# methods
def sum(a, b):
    print(a+b)
    
x = sum(20,30)

x = 5
y = 2.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

# casting
x = int(2) # 2
y = int(2.5) # 2
z = float(1) # 1.0
p = str(10) # "10"

print(x)
print(y)
print(z)
print(p)

# string
x = "Hello world.."
print(x[6:11])
print(len)
print(x.lower())

x = "  Hello,world.."
print(x.strip())
print(x.replace("e", "a"))
print(x.split(","))

print("enter your name:  ")
x = input()
print("Hello, " + x)
