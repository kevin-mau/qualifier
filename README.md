# Loan Qualifier Application
A fintech tool that analyzes a rate sheet and returns the loans that a borrower is qualified for.
---

## This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
    Rate sheet is stored in: data\daily_rate_sheet.csv
    * enter credit score
    * enter amount of monthly debt
    * enter monthly income
    * enter desired loan amount
    * finally enter in the home value

    The loan qualifier will determine your monthly debt to income ratio, as well as the loan to value ratio.  It will also determine which bank loans you are qualifed for.  If you're a qualified borrower, you will have the option to save the loans that you are qualified for in a CSV file.

    The CSV output will be stored in data\qualifed.csv by default.

---