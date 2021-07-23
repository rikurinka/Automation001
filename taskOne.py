"""
ual = eval(input("Enter the vishnu annual salary: "))
sal= ual/12
print("Vishnu monthly salary: ", sal)
"""
"""
30days - unlimited -100 Mbps
699 +GSt
"""

"""
Amazon / brandfactory - kidswear Flatt 55% offer
"""

"""
consider plan cost is rs699, gst is 18%, now calculate
final cost of plan
"""

planCost = 699
gst = 18
gstAmt = planCost * gst/100
finalPlanCost = planCost+gstAmt
print("Plan cost is: ", planCost)
print("Gst         : ", gst, "%")
print("Gst Amount  : ",gstAmt)
print("Final Cost is: ", finalPlanCost)

"""
dynamic

Read pendrive cost, and discount, then calculate final cost
of pendrive?

discounted_price = original_price - (original_price * discount / 100)

"""

pdCost = eval(input("Enter the pendrive cost: "))
discount = eval(input("Enter discount: "))
discountAmt = pdCost * discount/100
finalCost = pdCost - discountAmt
print("Pendrive cost : ",pdCost)
print("Discount      : ", discount, "%")
print("DiscountAmt   : ", discountAmt)
print("Final cost    : ", finalCost)


"""
Read Employee monthly salary, employee has to pay tax as 15%,
so calculate his final monthly salary
"""

empA_MonSal = eval(input("Enter Employee A monthly salary: "))
empA_AnnSal = empA_MonSal * 12
empA_PayTax = empA_AnnSal * 15 / 100
empA_Total = empA_AnnSal - empA_PayTax
empA_FinalSalary = empA_Total/12
print("Employee Annual Salary before tax: ", empA_AnnSal)
print("Employee tax payable amount      : ", empA_PayTax)
print("Employee Total Annual Salary     : ", empA_Total)
print("Employee Final monthly Salary    : ", empA_FinalSalary)
