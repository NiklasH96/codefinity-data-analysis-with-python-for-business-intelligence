def automate_regional_analysis(north_sales, south_sales):
    north_clean = clean_sales_data(north_sales)
    south_clean = clean_sales_data(south_sales)

    north_totals = summarize_sales(north_clean)
    south_totals = summarize_sales(south_clean)

    north_report = generate_report("North", north_totals)
    south_report = generate_report('South', south_totals)
    
    return {"North": north_report, "South": south_report}
    
def clean_sales_data(records):
    cleaned = []
    for record in records:
        if not isinstance(record, dict):
            continue

        product = record.get('product')
        sales = record.get('sales')
        
        if not product:
            continue
        if sales is None:
            continue
        try:
            sales_value = float(sales)
        except(ValueError, TypeError):
            continue

        cleaned.append({'product': product, 'sales': sales_value})

    return cleaned

def summarize_sales(cleanded_records):
    total_sales = {}
    for record in cleanded_records:
        product = record['product']
        sales = record['sales']
        total_sales[product] = total_sales.get(product, 0) + sales

    return total_sales

def generate_report(region, totals):
    list = [f'Sales Report for {region} Region:']
    if not totals:
        list.append('No valid sales data.')
    else:
        for product, total in totals.items():
            list.append( f'{product}: {total:.2f}')

    return '\n'.join(list)

north_sales = [
    {"product": "Widget", "sales": "100.5"},
    {"product": "Gadget", "sales": 85},
    {"product": "Widget", "sales": "invalid"},
    {"product": "Gizmo", "sales": 50},
    {"product": None, "sales": 30},
    "not a dict",
    {"product": "Widget", "sales": 25.0}
]

south_sales = [
    {"product": "Widget", "sales": "75"},
    {"product": "Gadget", "sales": 95.5},
    {"product": "", "sales": 20},
    {"product": "Gizmo", "sales": None},
    {"product": "Gadget", "sales": "10"},
    {"product": "Widget", "sales": 40}
]

result = automate_regional_analysis(north_sales, south_sales)
north_report = result["North"]
south_report = result["South"]
print(north_report)
print(south_report)