#lex_auth_012693711503400960120

def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if(num1==7):
        num1=1 
    if(num2==7):
        num1=1 
        num2=1 
    if(num3==7):
        return -1
    product=num1*num2*num3
    return product
        
    

#Provide different values for num1, num2, num3 and test your program
product=find_product(4,2,7)
print(product)