#input a sentence reverse it
'''
sentence=str(input("enter string\n"))

#sentence--->list (split)

l=sentence.split(' ')

print(l)

list_reverse=l[::-1]
print(list_reverse)

#list---->string(join)

join_list=' '.join(list_reverse)

print(join_list)


#i have a list ["python","is","easy"] , your task is to sentence 

'''

#palindrome
'''
sentence=input("enter a string\n")

if sentence[::-1]==sentence:

    print("yes")
else:
    print("no")
'''
'''
#finding ith char in string

sentence="geeksforgeeks"

char_to_be_remove=input("input char")
new=sentence.replace(char_to_be_remove,"")
print(new)

#replace(character to be replaced,new character)



#string methods
#upper()
#lower()
#strip(),lstrip(),rstrip()
#find()
#replace()
#swapcase()

new_sentence="GeeKs"
print(new_sentence.swapcase())

'''
'''
#check if substring is present in string,return its index too

sentence="geeksforgeeks"
sub="for"

if sub in sentence:
    print("yes at index",sentence.find(sub))

else:
    print("no")

'''
'''
#find length of string in python
sentence="geeksfoegeeks"

print(len(sentence))

#second way

count=0

for char in sentence:
    count=count+1

print(count)
'''
'''
sentence="i dont like java at all"

s=sentence.split(' ')
print(s)

for i in s:
    if len(i)%2==0:
        print(i)

'''

#vowels in sentence

#1.check if vowels are present in a string
#2check and count vowels in string
#3 accept only strings that have vowels in it

#vowels=a,e,i,o,u
'''
sentence="geeksforgeeks"
vowels=["a","e","i","o","u"]
for i in sentence:

    if i in vowels:
        print("yes")
    else:
        print("no")

   '''

'''
from collections import Counter

sentence="geeksforgeeks"

vowels=["a","e","i","o","u"]

l=[]


for i in sentence:
    l.append(i)
print(l)

for j in l:
    if j in vowels:
        print(Counter(j))

'''
'''
sentence="geeksforgeeks"

vowels=["a","e","i","o","u"]

for i in sentence:
    if i in vowels:
        print("string accepted")

    else:
        print("not accepted")


'''