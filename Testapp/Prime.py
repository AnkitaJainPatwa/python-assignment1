A = int(input("please enter the number"))

if A>1:
    for i in range(2,A):

        if(A%i)== 0:
             print(A,"number is not prime")
            # print(i, "times", A // i, "is", A)
             break
    else:
            print("Number is prime")

else:
    print("Number is not prime")


print("-------------n interval of prime")

N=int(input("please enter the number"))
for val in range(0,N):
    if val>1:
        for i in range(2,val):

            if(val%i)==0 :
                break

        else:
                print(val)