#factors
#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap to display factors of a number


n=int(input("enter number:\n"))

for i in range(1,n+1):
    if n%i==0:
        print(i)