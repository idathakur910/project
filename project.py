principal_amount = 10000
time = 4
rate_of_interest = 14

# calculate the simple interest
simple_interest = (principal_amount * time * rate_of_interest)/100

print("Simple interest is: ", simple_interest)


# calculate the simple interest
compound_interest = principal_amount * ((1 + rate_of_interest / 100)**time - 1)

print("Compound interest is: ", compound_interest)