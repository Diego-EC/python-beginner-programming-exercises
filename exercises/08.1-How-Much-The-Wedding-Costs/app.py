user_input = int(input('How many people are coming to your wedding?\n'))

if user_input > 200:
    price = "20000"
elif user_input > 100:
    price = "15000"
elif user_input > 50:
    price = "10000"
else:
    price = "4000"

#if user_input < 50:
#    price = 4000 

print('Your wedding will cost '+str(price)+' dollars')

