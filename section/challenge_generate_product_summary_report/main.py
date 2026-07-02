def generate_product_report(summary_dict):
    report = ''
    total_revenue = 0
    for product, data in summary_dict.items():
        report += f'Product: {product}, Units Sold: {data["units_sold"]}, Revenue: ${data["revenue"]:.2f}\n'
        total_revenue += data['revenue']
        
    report += f'Total Revenue: ${total_revenue:.2f}\n'
        
    return report

summary = {
    "Widget": {"units_sold": 120, "revenue": 2400.00},
    "Gadget": {"units_sold": 75, "revenue": 1500.50},
    "Thingamajig": {"units_sold": 200, "revenue": 5000.00}
}
report = generate_product_report(summary)
print(report)
