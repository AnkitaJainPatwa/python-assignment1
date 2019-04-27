list = []

num=int(input("Enter number u want to enter "))

for i in range(num):
    numbers=int(input("enter number"))
    list.append(numbers)

print("Maximum number of elements :",max(list), "/n Minimum number of element in list",min(list))


