import pandas as pd
import random
from faker import Faker

fake = Faker()

# Customers table
def generate_customers(n=10000):
    data = []
    plans = ['Prepaid', 'Postpaid']
    for i in range(1, n + 1):
        data.append([
            i,
            fake.name(),
            fake.email(),
            fake.phone_number(),
            fake.date_between(start_date='-2y', end_date='today'),
            random.choice(plans)
        ])
    df = pd.DataFrame(data, columns=['customer_id', 'name', 'email', 'phone', 'signup_date', 'plan_type'])
    df.to_csv('customers.csv', index=False)
    print("✅ customers.csv created")

# Usage table
def generate_usage(n=20000):
    data = []
    for i in range(1, n + 1):
        data.append([
            i,
            random.randint(1, 10000),
            round(random.uniform(0, 500), 2),  # call_minutes
            round(random.uniform(0, 100), 2),  # data_used_gb
            random.randint(0, 500),  # sms_count
            fake.date_between(start_date='-1y', end_date='today')
        ])
    df = pd.DataFrame(data, columns=['usage_id', 'customer_id', 'call_minutes', 'data_used_gb', 'sms_count', 'usage_date'])
    df.to_csv('usage.csv', index=False)
    print("✅ usage.csv created")

# Billing table
def generate_billing(n=20000):
    data = []
    statuses = ['Paid', 'Due', 'Overdue']
    for i in range(1, n + 1):
        customer_id = random.randint(1, 10000)
        amount = round(random.uniform(10, 500), 2)
        bill_date = fake.date_between(start_date='-1y', end_date='today')
        due_date = bill_date + pd.Timedelta(days=30)
        payment_status = random.choice(statuses)
        data.append([
            i,
            customer_id,
            bill_date,
            amount,
            payment_status,
            due_date
        ])
    df = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'bill_date', 'amount', 'payment_status', 'due_date'])
    df.to_csv('billing.csv', index=False)
    print("✅ billing.csv created")

# Run all generators
generate_customers()
generate_usage()
generate_billing()
