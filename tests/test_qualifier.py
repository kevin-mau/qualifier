import csv
# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size
def test_save_csv():
    path = Path('data\output\qualifying_loans.csv')
    assert (path).exists()
def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375
def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('data\daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000
'''
    assert len(credit_score(current_credit_score, bank_data)) == 6
    monthly_debt_ratio = 0.375
    assert len(debt_to_income(monthly_debt_ratio, bank_data)) == 6
    loan_to_value_ratio = 0.84
    assert len(loan_to_value(loan_to_value_ratio, bank_data)) == 6
    assert len(max_loan_size(loan, bank_data)) == 6
'''
    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
'''    
    output =  Path('data\output\qualifying_loans.csv')
    assert len(fileio.save_csv(bank_data, output, True)) == 24
'''    

