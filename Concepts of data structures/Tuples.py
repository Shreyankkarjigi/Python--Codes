#tuples
'''
denoted by ()
ordered 
immutable(doesnt allow add/update/delete of elements)
indexed
support multiple data types
allows duplicates

operations on tuples:

1.Access elements
2.slicing 
3.striding
4.delete (entire tuple)
5.concat
6.Iterable
7.Faster than lists

#Initalizing tuples

number=(1,2,3,4,5)
char=("a","b","c")
both=(1,2,3,"a","b")


#To know index of some element 
#enumerate(to find index of element in iterable object)

for element in enumerate(char):
    print(element)

output 

(0, 'a')
(1, 'b')
(2, 'c')


#Allows duplicates
numbers=(1,1,"a","a")

#Concat tuples
add=number+char
print(add)

#Slicing

#rule of index
#[index:index-1]  for example if we want to access till index 0 to 3 we need to pass index value as [0:4]

num=(1,2,4,5)
print(num[0:3])#index
print(num[1])#single element acess
print(num[-1])#last element
print(num[::-1])#reverse tuples

#Striding

#[start:end:steps]

t1=(1,2,3,4,5,6,7,8)
#print every second element
print(t1[1:7:2])
t=(1,2,3,4,4,5,56,6,6)
print(t[::-5])

'''