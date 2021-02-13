def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    ticket_number = 101
    ticket_str = ""
    #Write your logic here

    while no_of_passengers != 0:
        ticket_str = airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(ticket_number)
        ticket_number_list.append(ticket_str)
        ticket_number += 1
        no_of_passengers -= 1



    #Use the below return statement wherever applicable
    return ticket_number_list if len(ticket_number_list) < 5 else ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))