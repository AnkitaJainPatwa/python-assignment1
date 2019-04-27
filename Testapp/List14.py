a_empid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = ["ram", "shyam", "hari", "Tony", "sita", "gita", "monu", "shanu", "rita", "kittu"]



print(a_empid)

print(b)

for i in range(len(a_empid)):
    print(i,end="  ")

    print(a_empid[i])

print ("Please enter elements of other list with indices")

for j in range(len(b)):
    print(j,end=" ")

    print(b[j])

#from operator import itemgetter
print (a_empid[4:9])
print("-----------")

print(b[4:9])

print("----------")

print(a_empid[3:len(a_empid)])
print("-------------")

print(b[3:len(b)])

print("###########")

i=int(input("please enter the number"))

for j in range(len(b)):
    print(end=" ")
    print(i*b[j])
    print(end=" ")

print("--------- CONCATENATE")

a_empid1 = a_empid + b

print("Concatenate of two list"+str(a_empid1))
