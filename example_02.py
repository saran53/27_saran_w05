def calcurate_salary(salary,ot_time,ot_rate,tax):
    gross_pay = salary + (ot_time * ot_rate)
    tax_pay = gross_pay * tax
    net_pay = gross_pay - tax_pay
    return net_pay, tax_pay, gross_pay

emp_1 = calcurate_salary(15000,10,200,0.07)

print(emp_1)