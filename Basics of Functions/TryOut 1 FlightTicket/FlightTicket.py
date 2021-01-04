#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adult_rate = 37550.0 
    child_rate = adult_rate/3 
    stax = 7/100
    season_discount = 10/100
    
    #using Successive percentage method GRE
    final_tax_discount =  (1 + stax) * (1 - season_discount) # = 0.963
    
    total_ticket_cost = (adult_rate * no_of_adults + child_rate * no_of_children) * final_tax_discount
    

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)