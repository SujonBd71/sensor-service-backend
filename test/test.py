account_value = 0 
deposite = 19200
current_age = 20 
retirement_age = 67
int_rate = 13.764
num_of_calculations = retirement_age - current_age

principal = deposite
for iteration in range(num_of_calculations): 
    interest= principal * int_rate / 100.0
    new_account_value= principal + interest
    print(iteration, deposite, new_account_value)
    principal = new_account_value
