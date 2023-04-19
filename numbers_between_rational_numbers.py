#To print n number of rational numbers between x and y where x and y are rational numbers

c = 0
listA = []

def methodA(a, b, numbers):
    for i in range(numbers):
        c = (a + b)/2
        listA.append(c)
        b = c
    print(listA)
    
    

a1 = int(input("Enter the numerator of the smaller fraction: "))
a2 = int(input("Enter the denominator of the the smaller fraction: "))

b1 = int(input("Enter the numerator of the larger fraction: "))
b2 = int(input("Enter the denominator of the the larger fraction: "))

numbers = int(input("Enter the number of numbers you want: "))
a = a1/a2
b = b1/b2

methodA(a, b, numbers)