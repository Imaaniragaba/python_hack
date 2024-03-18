a = 0
b = 1
your_number = input("Enter Number: ")

for i in range(int(your_number)):
    print(a)

    a,b = b, a+b
    
    