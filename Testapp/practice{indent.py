num = int(input("Enter number of rows"))
row=0

while row<num :
    space=num-row-1

    while space>0:


        print(end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
#while row==num :
 #   space=num-row-0

    while space>0:
        print(end=" ")
        #row=row-1
        space=space+1
        star=row-1
    while star==num:
        print("*",end=" ")
        star=star+1
        row=row-1
        print()


