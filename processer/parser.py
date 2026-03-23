import re
import pandas as pd

def parse_transactions(text):
    """
    Parse transaction lines from PDF text into a DataFrame.
    Returns columns: Date, Description, Amount.
    """
    lines = text.split("\n")
    transactions = []

    # Basic regex for example; adjust based on your bank statement format
    for line in lines:
        match = re.search(r"(\d{2}/\d{2}/\d{4}).+?([-\$]?\d+[.,]?\d*)", line)
        if match:
            date = match.group(1)
            amount = match.group(2)
            description = line.replace(date, "").replace(amount, "").strip()
            transactions.append({"Date": date, "Description": description, "Amount": amount})

    df = pd.DataFrame(transactions)
    return df