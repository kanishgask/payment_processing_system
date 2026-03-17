class TransactionService:

    def __init__(self):
        self.transactions = []

    def record_transaction(self, payment_id, amount):

        transaction = {
            "payment_id": payment_id,
            "amount": amount,
            "status": "RECORDED"
        }

        self.transactions.append(transaction)

        return transaction
