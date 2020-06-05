#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem
#print even numbers and odd numbers in a certain range

r=int(input("enter range"))
#loop for even
print("Even numbers")
for i in range(r):
    if i%2==0:
        print(i)

print("Odd numbers")

for i in range(r):
    if i%2!=0:
        print(i)
   

'''
output

enter range10
Even numbers
0
2
4
6
8
Odd numbers
1
3
5
7
9
'''


   

  