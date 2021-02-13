def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    if num1 >= num2:
        return -1
    
    num_list = []
    
    for i in range(num1,num2+1):
        if len(str(i)) == 2:
            if (int(str(i)[0])+int(str(i)[1]))%3 == 0:
                if i%5 == 0:
                    num_list.append(i)

    max_num = num_list[-1] if len(num_list) > 0 else -1

    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(2,14)
print(max_num)