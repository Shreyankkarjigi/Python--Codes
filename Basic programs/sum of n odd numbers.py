#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
print sum of n odd numbers, take n from user

'''

n=int(input("enter range"))
sum=0

for i in range(n):
    if i%2==1:
       sum=sum+i
print("sum of n odd numbers is:",sum)


'''
output
sum of n odd numbers is: 25

'''
