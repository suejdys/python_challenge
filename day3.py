# Write your code here:
def get_yearly_revenue(monthly_revenue):    #연간 매출 계산
    revenue_for_a_year = monthly_revenue * 12   #월간매출 인수 * 12 = 1년
    return revenue_for_a_year       #연간 매출 리턴

def get_yearly_expenses(monthly_expense):    #연간 비용 계산
    expense_for_a_year = monthly_expense * 12       #월간비용 인수 * 12 = 1년
    return expense_for_a_year       #연간 비용 리턴

def get_tax_amount(profit):
    tax_amount = 0
    if(profit>1000000):     
        tax_amount += profit * 0.25     #profit이 1000000이상이면 0.25곱해줌
    else:
        tax_amount += profit * 0.15     #아니면 0.15 곱함
    return tax_amount

def apply_tax_credits(tax_amount, tax_credits):
    discount = tax_amount * tax_credits     #tax_amount*tax_credit = 할인금액
    return discount     #리턴

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")