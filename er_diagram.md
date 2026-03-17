# ER Diagram – Payment Processing System

USERS
- user_id
- name

PAYMENTS
- payment_id
- user_id
- amount
- status

TRANSACTIONS
- transaction_id
- payment_id
- amount
- status

Relationships

User 1 → N Payments  
Payment 1 → 1 Transaction
