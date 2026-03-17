class PaymentService:

    def __init__(self):
        self.payments = []
        self.payment_id = 0

    def process_payment(self, user_id, amount):

        self.payment_id += 1

        payment = {
            "payment_id": self.payment_id,
            "user_id": user_id,
            "amount": amount,
            "status": "PROCESSING"
        }

        self.payments.append(payment)

        return payment

    def complete_payment(self, payment_id):

        for payment in self.payments:

            if payment["payment_id"] == payment_id:
                payment["status"] = "SUCCESS"

        return "Payment Completed"
