def clean_sales_data(sales_records):
    clean_records = []
    
    for record in sales_records:
        clean_record_copy = record.copy()
        if clean_record_copy['units_sold'] == None:
            clean_record_copy['units_sold'] = 0
        if clean_record_copy['revenue'] == None:
            clean_record_copy['revenue'] = 0
        clean_record_copy['product'] = clean_record_copy['product'].title()
        clean_records.append(clean_record_copy)
        
    return clean_records

sales_data = [
    {'date': '2024-06-01', 'product': 'laptop', 'units_sold': 10, 'revenue': 15000},
    {'date': '2024-06-02', 'product': 'Laptop', 'units_sold': None, 'revenue': 14500},
    {'date': '2024-06-03', 'product': 'tablet', 'units_sold': 5, 'revenue': None},
    {'date': '2024-06-04', 'product': 'SMARTphone', 'units_sold': None, 'revenue': None},
]

cleaned_sales = clean_sales_data(sales_data)
print(cleaned_sales)
