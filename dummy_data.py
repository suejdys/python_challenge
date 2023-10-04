def tax_calc(money):    
    return money * 0.35     #return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_calc("suhyeok")    #return value => to_pay variable 
pay_tax(to_pay)