import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('customer_data.csv')
data['Total'] = data['Quantity'] * data['Price']

customer_total = data.groupby('Name')['Total'].sum().reset_index()
product_count = data.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
top_customers = customer_total.sort_values(by='Total', ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=product_count.index, y=product_count.values, palette='viridis')
plt.title('Product Popularity by Quantity Sold')
plt.ylabel('Quantity Sold')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('screenshots/bar_chart.png')
plt.show()

revenue_by_product = data.groupby('Product')['Total'].sum()
plt.figure(figsize=(6,6))
plt.pie(revenue_by_product, labels=revenue_by_product.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Revenue Share by Product')
plt.tight_layout()
plt.savefig('screenshots/pie_chart.png')
plt.show()

print("Customer Total Purchases:")
print(customer_total)
print("\nTop Customers:")
print(top_customers)
print("\nMost Popular Products:")
print(product_count)
