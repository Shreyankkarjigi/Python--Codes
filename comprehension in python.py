#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
#comprehension in python

'''
list_variable = [x for x in iterable]

'''

'''
suppose you want to generate a list of numbers containing odd numbers from 1-10

here is the traditonal way to do it
'''
odd=[]

for i in range(10):
    if i%2==1:
        odd.append(i)
print(odd)

'''
output

[1, 3, 5, 7, 9]
'''
'''
But there is a smarter way to do it using list

'''
odd_number=[]

odd_number=[i for i in range(10) if i%2==1]

print(odd_number)

