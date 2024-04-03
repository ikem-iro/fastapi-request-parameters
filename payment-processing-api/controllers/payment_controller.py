

def complete_transaction(payment_details):
    """
    Complete a transaction using the provided payment details.

    Parameters:
    - payment_details: a dictionary containing the amount and any additional charges

    Returns:
    - If the transaction is successful, returns a dictionary with a success message
    - If the transaction fails due to insufficient funds, returns a dictionary with an error message
    """
    balance = 5000
    charges = 3.5
    amount_to_debit = payment_details.amount + charges
    if amount_to_debit >= balance:
        return{"error": "transaction could not be completed"}
    return {"message": "transaction completed"}