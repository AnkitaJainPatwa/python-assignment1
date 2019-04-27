list1=['1','2','3','4','5']

check='5'
result=check in list1

print("Result",result)

print('-----------------element existence check without in operator')

for i in list1:
    if (i == '5'):

        print("element exist")

print('--------print list in reverse direction')

list1.reverse()
print(list1)
