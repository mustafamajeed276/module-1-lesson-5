actual_cost = float(input("enter the actual amount"))
sales_cost = float(input("enter the sales amount"))
if (actual_cost < sales_cost):
 amount = sales_cost - actual_cost
 print("total profit = {0}".format(amount))
else:
  print("no profit??!!!")