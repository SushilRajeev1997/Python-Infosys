
def get_count(num_list):
    count=0

    # Write your logic here

    max_len = len(num_list)
    for i in range(0,max_len):
        if i+1 != max_len:
            if num_list[i] == num_list[i+1]:
                count+=1
        

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))