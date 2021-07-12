# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans, output, save_csv_answer):
    """Writes the CSV file to the path provided.
    
    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
        output: the filepath destination of where the CSV should be saved.
        save_csv_answer: This is the user's answer (from the save_qualifying_loans function) whether to save the CSV or not.
        If they answered Yes, then answer is True, and save_csv function will save the CSV.       
        
    """
    if save_csv_answer == True:
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    # Set the output file path
        output_path = Path(output)

    # Using the csv library and `csv.writer` to write the header row
    # and each row of banks from the `qualifying_loans` list.
    
        with open(output_path, "w") as csvfile:
            #create a csvwriter
            csvwriter = csv.writer(csvfile, delimiter=",")
            #writing the header to CSV file first
            csvwriter.writerow(header)
            #writing the values to each row in the CSV
            for row in qualifying_loans:
                csvwriter.writerow(row) 

            # if save_csv function writes CSV then it will return True.
            return True