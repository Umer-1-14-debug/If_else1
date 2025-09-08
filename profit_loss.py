cost_value=float(input("Enter the cost price of the object."))
selling_value=float(input("Enter the selling price of the object"))
profit=selling_value-cost_value
loss=cost_value-selling_value
if selling_value>cost_value:
    print("You have earned a profit of "+profit)
else:
    print("You have a loss of "+str(loss))