#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to check amstrong number

#input number from user
n=int(input("Enter number:\n"))

#initialize sum as 0

sum=0

#store n in a temp variable, all operation occurs on temp variable and not on original number
temp=n
#initalise a while loop

while temp>0:

    #separate the digits using reminder method

    digits=temp%10

    #compute the digit power 3

    sum=sum+digits**3

    #divide the original number by 10 to convert it for next iteration

    temp=temp//10


    #check if temp==sum if yes print amstrong else not


if n==sum:
   print("amstrong")
    
else:
    print("not")