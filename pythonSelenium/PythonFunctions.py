def print_hello():
    print("hello")

print_hello()

def printHi(name="elias"):
    print("Hi, "+name)
    
printHi("Omar")
printHi()

def sum(a,b,c):
    print(a+b+c)
sum(10,20,30)

def returnSum(a,b):
    return (a+b)

x = returnSum(10,20)
print(x)