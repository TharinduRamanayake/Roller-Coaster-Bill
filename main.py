height = float(input ("Enter Your Height (cm)? "))
bill = 0

if (height >= 120):
    print ("You can Ride")
    age = int (input("Enter Your Age? "))
    
    if (age <=  12):
        bill = 5
        print ("Childern tickets are $5")
        
    elif (12 < age and age < 18):
        bill = 7
        print ("Youth tickets are $7")
        
    elif (45 < age and age < 55):
        bill = 0
        print ("Everything is going to be ok. You have a free ride!")
        
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
