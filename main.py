#TharinduRamanayake

height = float(input ("Enter Your Height (cm)? "))
bill = 0

if (height >= 120):
    print ("You can Ride")
    age = int (input("Enter Your Age? "))
    
    if (age <=  12):
        bill = 5
        print ("Childern tickets are $5")
        
    elif (12 < age > 18):
        bill = 7
        print ("Youth tickets are $7")
        
    else:
        bill = 12
        print ("Adult tickets are $12")
        
        
    photo = input ("If You want Photos? (Y or N) ")
    if photo == "Y" or "y":
        new_bill = bill + 3
        print (f"Your Final Bill is ${new_bill}.")
    else:
        print (f"Your Final Bill is ${bill}.")
else:
    print ("You can't Ride")
