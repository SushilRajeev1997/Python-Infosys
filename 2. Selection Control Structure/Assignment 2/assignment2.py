def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed

    five_needed = rupees_to_make // 5
    one_needed = rupees_to_make % 5


    flag = False

    if(five_needed <= no_of_five and one_needed <= no_of_one):
        flag = True
    elif(five_needed > no_of_five and one_needed < no_of_one):
        five_needed = no_of_five
        one_needed = rupees_to_make - (five_needed * 5)
        
        if(five_needed <= no_of_five and one_needed <= no_of_one):
            flag = True
    
   

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    if(flag):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105,20,5)