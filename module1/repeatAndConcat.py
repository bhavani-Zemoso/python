def rep_cat(num1, num2):
    return (str(num1) * 10) + (str(num2) * 5)

print(rep_cat(3,4))
rep_cat_lambda = lambda num1, num2: (str(num1) * 10) + (str(num2) * 5)
print(rep_cat_lambda(2,7))