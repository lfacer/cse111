from datetime import datetime

current_date_and_time = datetime.now()

#weekday where Monday=0 and Sunday=6
day_of_week = current_date_and_time.weekday()

subtotal = True

while subtotal > 0:
    
    subtotal = float(input("Please enter the subtotal: "))

    #discount total
    if day_of_week == 1 or 2 and subtotal >= 50:
        discount = subtotal * 0.1
        discount_total = subtotal - discount
        sales_tax = discount_total * 0.06

        total = discount_total + sales_tax

        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

    #stretch challenge
    elif day_of_week == 1 or 2 and subtotal <= 50:
        if subtotal == 0:
            break
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        missed_discount = 50 - total

        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print(f"On Tuesdays and Wednesdays if you spend $50 or more you get 10% of your purchase! You were ${missed_discount:.2f} away from the discount :(")


    #non-discount total
    else:
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")