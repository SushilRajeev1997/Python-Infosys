def find_leap_years(given_year):

    # Write your logic here

    list_of_leap_years = []
     
    while len(list_of_leap_years) < 15:
        is_leap = (((given_year % 4 == 0) and (given_year % 100 != 0)) or (given_year % 400 == 0))
        if is_leap:
            list_of_leap_years.append(given_year)
        given_year += 1

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)