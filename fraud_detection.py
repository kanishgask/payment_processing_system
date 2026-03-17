class FraudDetection:

    def check_transaction(self, amount):

        if amount > 10000:
            return "FLAGGED"

        return "APPROVED"
