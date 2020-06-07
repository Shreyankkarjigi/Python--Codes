#print even numbers
even=[i for i in range(10) if i%2==0]
print(even)
#print odd numbers
odd=[i for i in range(10)if i%2!=0]
print(odd)
#print sqaures of even numbers from 1 to 10
even_squares=[i**2 for i in range(10) if i%2==0]
print(even_squares)
#print sqaures of odd numbers for 1 to 10
odd_sqaures=[i**2 for i in range(10) if i%2!=0]
print(odd_sqaures)
#print numbers from 1 to 10 in steps of 2
skip=[i for i in range(0,10,2)]
print(skip)
