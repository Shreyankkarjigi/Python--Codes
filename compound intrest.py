#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
'''
print product of n numbers, take n from user

'''

n=int(input("enter range"))

#can't multiply number with 0 so prod=1


prod=1

for i in range(1,n):
    prod=prod*i

print("Product is",prod)


'''
output

enter range10
Product is 362880

'''