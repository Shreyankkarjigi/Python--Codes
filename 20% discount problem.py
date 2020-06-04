#Code by Shreyank #Github-https://github.com/Shreyankkarjigi
#problem: Wap for a shopping cart
#take total items from user
#if item price is above or equal give 20% discount
#display the item quantity and its price
#display total bill



n=int(input("enter total items"))
list_quantity=[]
list_price=[]
list_100=[]
list_not100=[]

#input quantity

for i in range(n):
    quan=int(input("enter quantity"))

    #append to list_quantity

    list_quantity.append(quan)

    #display items

print("quanity summary:")
print(list_quantity)

#input price
#direct check price for above = 100
#if above equal 100 append to list_100 else append to list_not 100
#apply 20 % discount directly 

for j in range(n):

    price=int(input("enter price of items"))

    if price>=100:
        print("prices above or equal to 100 INR detected,applying 20 percent discount")
        new_price= price//10 * 2

        #append this to list_100 above

        list_100.append(new_price)
     

    else:
        list_not100.append(price)

        

total=sum(list_100+list_not100)


print("total bill to be paid",total,"INR")
print("Thank you for shopping with us, hope to never see you again :)")


'''
output

enter total items5
enter quantity1
enter quantity2
enter quantity3
enter quantity4
enter quantity5
quanity summary:
[1, 2, 3, 4, 5]
enter price of items100
prices above or equal to 100 INR detected,applying 20 percent discount
enter price of items22
enter price of items30
enter price of items400
prices above or equal to 100 INR detected,applying 20 percent discount
enter price of items500
prices above or equal to 100 INR detected,applying 20 percent discount
total bill to be paid 252 INR
Thank you for shopping with us, hope to never see you again :)


'''