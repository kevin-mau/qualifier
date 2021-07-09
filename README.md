# *Loan Qualifier Application*
---
### This fintech tool written in python analyzes a rate sheet along with the borrower's information, then returns the bank loans that the borrower can qualify for.  The Loan Qualifier Application is a command line application where the borrower will enter their information and can choose to receive a CSV output of their qualified loans. 
---
## Technologies:

This application utilizes python 3.7 along with the packages below:

* [fire](https://github.com/google/python-fire) - This is for the command line interface.

* [questionary](https://github.com/tmbo/questionary) - This makes it an interactive user experience to gather their loan data for the application.
---
## Installation Guide

Prior to running the application, you will need to install these dependencies:

```python
  pip install fire
  pip install questionary
```

## Instructions:

Clone the repository and then in your command line run the python application: **app.py**

It will first ask you the file path to the daily rate sheet.

The rate sheet is stored in: [data\daily_rate_sheet.csv](https://github.com/kevin-mau/qualifier/blob/main/data/daily_rate_sheet.csv)

Then enter the following information for the potential borrower:

* credit score
* amount of monthly debt
* monthly income
* desired loan amount
* the home value

The loan qualifier will determine the borrower's monthly debt-to-income ratio and the loan-to-value ratio of their mortgage loan.  It will also determine which bank loans the borrower will qualify for.  

If the borrower qualifies for any of the bank loans offered on the rate sheet, you will have the option to save and view the list of approved loans on a CSV file output.  The CSV output should be stored in: [data\output\qualifed_loans.csv](https://github.com/kevin-mau/qualifier/blob/main/data/output/qualifying_loans.csv)

---

## Contributors

kevin-mau

---

## License

MIT