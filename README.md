# *Loan Qualifier Application*
---
### A fintech tool that analyzes a rate sheet, then returns the bank loans that the borrower can qualify for.  This is a command line application where the borrower will enter their information and can choose to receive a CSV output of their qualified loans. 
---
**Instructions:**
run $ python app.py

the Rate sheet is stored in: data\daily_rate_sheet.csv

* enter credit score
* enter amount of monthly debt
* enter monthly income
* enter desired loan amount
* finally enter in the home value

The loan qualifier will determine your monthly debt to income ratio, as well as the loan to value ratio.  
It will also determine which bank loans you are qualifed for.  

If you're a qualified borrower, you will have the option to save the loans that you are qualified for into a CSV file.  The CSV output should be stored in: data\output\qualifed_loans.csv    

---