def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    valid_loan_sal = True
    loan_eligibility = False
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    if (loan_type == "Car" and salary > 25000):
        eligible_loan_amount = 500000 
        bank_emi_expected = 36
    elif (loan_type == "House" and salary > 50000):
        eligible_loan_amount = 6000000
        bank_emi_expected = 60
    elif (loan_type == "Business" and salary > 75000):
        eligible_loan_amount = 7500000
        bank_emi_expected = 84
    else:
        valid_loan_sal = False

    valid_acc = False
    
    if(len(str(account_number))==4 and str(account_number)[0] == "1"):
        valid_acc = True
        
    
    valid_min_balance = False
    
    if(account_balance>=100000):
        valid_min_balance = True

    if(eligible_loan_amount >= loan_amount_expected and bank_emi_expected >= customer_emi_expected):
        loan_eligibility = True

    flag = valid_acc and valid_min_balance and valid_loan_sal and loan_eligibility

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work
    
    if(not flag):

        
        if(not valid_min_balance):
            print("Insufficient account balance")
        elif(not valid_acc):
            print("Invalid account number")
        elif(not valid_loan_sal):
            print("Invalid loan type or salary")
        elif(not loan_eligibility):
            print("The customer is not eligible for the loan")
        

    else:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)


    

#Test your code for different values and observe the results
calculate_loan(1005,30000,255000,"Car",300000,30)