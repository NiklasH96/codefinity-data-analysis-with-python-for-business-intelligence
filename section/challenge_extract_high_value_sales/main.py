def extract_high_value_sales(sales_records):
    high_value_sales = [{'date': record['date'],'product': record['product'],'revenue': record['revenue']}
                       for record in sales_records
                       if record['revenue'] > 1000]
    return high_value_sales

# Sample calls
sales_data = [
    {'date': '2024-06-01', 'product': 'Laptop', 'revenue': 1500, 'region': 'West'},
    {'date': '2024-06-01', 'product': 'Mouse', 'revenue': 200, 'region': 'East'},
    {'date': '2024-06-02', 'product': 'Monitor', 'revenue': 1200, 'region': 'North'},
    {'date': '2024-06-02', 'product': 'Keyboard', 'revenue': 700, 'region': 'South'}
]

result = extract_high_value_sales(sales_data)
print(result)