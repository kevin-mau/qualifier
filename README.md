# *Loan Qualifier Application*
---
### A fintech tool that analyzes a rate sheet, along with the borrower's information, then returns the bank loans that the borrower can qualify for.  This is a command line application where the borrower will enter their information and can choose to receive a CSV output of their qualified loans. 
---
**Instructions:**

In your command line run the python application: python app.py

the Rate sheet is stored in: [data\daily_rate_sheet.csv](data\daily_rate_sheet.csv)

Then enter the following information for the potential borrower:

* credit score
* amount of monthly debt
* monthly income
* desired loan amount
* the home value

The loan qualifier will determine the borrower's monthly debt-to-income ratio and the loan-to-value ratio of their mortgage loan.  
It will also determine which bank loans the borrower will qualify for.  

If the borrower qualifies for any of the bank loans offered on the rate sheet, you will have the option to save and view the list of approved loans on a CSV file output.  The CSV output should be stored in: [data\output\qualifed_loans.csv](data\output\qualifed_loans.csv)

---