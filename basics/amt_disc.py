amt = int(input('Enter the order amount'))
pm = (input('payment method (credit,cash,upi) : '))

if amt > 1000:
    disc = amt*3/100 # discount 3%
    amt = amt - disc
    print('Amount after discount')
    print(amt)
else:
    print('No discount')
    print(amt) 

if pm == 'credit': # discount Rs. 100 through credit card
        amt = amt - 100
        print('Payment from credit card')
        print(amt)
                
gst = amt*18/100 # GST 18%
amt = amt + gst
print('Your final amount using GST')
print(amt)

# OR, we can write our code in short form

amt = int(input('Enter amount'))
pm = input('payment method (credit,cash,upi) : ')
if amt > 1000:
    amt -= amt*.03 #discount 3%
if pm == 'credit':
    amt -= 100
amt += amt*.18 # GST 3%
print('Your final amount') 
print(amt)   