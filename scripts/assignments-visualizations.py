import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style='whitegrid')

# Load top 10 customers by billing
top_customers = pd.read_csv('/Users/karthikburra/Downloads/Assignment-Query-1.csv')

# Bar plot → Top 10 billed customers
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_customers.sort_values('total_billed', ascending=False),
    x='total_billed',
    y='name',
    palette='viridis'
)
plt.title('Top 10 Customers by Total Billing', fontsize=16, weight='bold')
plt.xlabel('Total Billed Amount ($)', fontsize=12)
plt.ylabel('Customer Name', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('/Users/karthikburra/Downloads/top_10_customers_improved.png')
plt.show()

# Load average data usage by plan type
avg_usage = pd.read_csv('/Users/karthikburra/Downloads/Assignment-Query-2.csv')

# Bar plot → Average data usage by plan type
plt.figure(figsize=(8, 5))
sns.barplot(
    data=avg_usage.sort_values('avg_data_usage', ascending=False),
    x='plan_type',
    y='avg_data_usage',
    palette='magma'
)
plt.title('Average Data Usage by Plan Type', fontsize=16, weight='bold')
plt.xlabel('Plan Type', fontsize=12)
plt.ylabel('Average Data Usage (GB)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('/Users/karthikburra/Downloads/avg_data_usage_by_plan_improved.png')
plt.show()