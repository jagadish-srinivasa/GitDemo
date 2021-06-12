price= (30,40,50)
p=f'''
food list:              Price:
    1. burger           {price[0]}
    2. pizza            {price[1]}
    3. patties          {price[2]}
'''
print(p)
a=int(input("Enter your choice:"))
b=int(input("Enter the quantity:"))
bill=price[a-1]*b
print(bill)



