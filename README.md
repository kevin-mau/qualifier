# *Loan Qualifier Application*
---
### The Loan Qualifier Application analyzes a rate sheet of banks alongside the borrower's loan information, then returns the number of mortgage loans that the borrower can qualify.  
### This fintech tool, that is written in python, is a command line application where the user will enter the borrower's data and can choose whether they want to receive a CSV output of their qualified mortgage loans. 
---
## Technologies:

This application utilizes python 3.7 along with the packages below:

* [fire](https://github.com/google/python-fire) - This is for the command line interface.

* [questionary](https://github.com/tmbo/questionary) - This makes it an interactive user experience to gather their loan data for the application.

* [pytest](https://docs.pytest.org/en/stable/) - For basic assertion testing of the program's calculations, filters, and file paths.

---
## Installation Guide

Prior to running the application, you will need to install these dependencies:

```python
  pip install fire
  pip install questionary
  pip install pytest
  pip install mkdocs
```

## Instructions:

Clone the repository and then in your command line run the python application **app.py** as such:

```python
python app.py
```

It will first ask you the file path to the daily rate sheet.

The rate sheet is stored in: [data\daily_rate_sheet.csv](https://github.com/kevin-mau/qualifier/blob/main/data/daily_rate_sheet.csv)

Then enter the following information for the potential borrower:

* credit score
* amount of monthly debt
* monthly income
* desired loan amount
* the home value

The loan qualifier will determine the borrower's monthly debt-to-income ratio and the loan-to-value ratio of their mortgage loan.  It will also determine which bank loans the borrower will qualify for.  

If the borrower qualifies for any of the bank loans offered on the rate sheet, you will have the option to save and view the list of approved loans on a CSV file output.  The CSV output should be stored in: [data\output\qualifying_loans.csv](https://github.com/kevin-mau/qualifier/blob/main/data/output/qualifying_loans.csv)

---

## Contributors

kevin-mau

---

## License

MIT