def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    
    bill_amount=0
    veg_price = 120
    non_veg_price = 150
    

    if(not(food_type in ["N","V"] and distance_in_kms > 0 and quantity_ordered >= 1)):
        return -1

    bill_amount = quantity_ordered * (veg_price if food_type == "V" else non_veg_price)
    
    if(distance_in_kms > 3 and distance_in_kms <= 6):
        bill_amount += (3 * (distance_in_kms-3))
    elif(distance_in_kms > 6):
        bill_amount += 9 + (6 * (distance_in_kms-6))
        

    #write your logic here
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",20,4)
print(bill_amount)