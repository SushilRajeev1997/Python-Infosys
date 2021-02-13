def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    # R + C = 35 --> heads
    # 4R + 2C = 94 --> legs
    #-- R = 12 AND C = 23
    #Populate the variables: chicken_count and rabbit_count

    # Let's look at invalid condition

    if legs%2 != 0 or heads == 0 or heads >= legs:
        print(error_msg)
    else:
        # since we know R+C=heads and 4R + 2C = legs
        #hence by reducing this equation we get R = (legs - 2heads)/2
        rabbit_count = (legs - 2 * heads)//2
        # we also know that C = heads - R, deduced from the above equation
        chicken_count = heads - rabbit_count
        print(chicken_count,rabbit_count)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(3,12)