from pathlib import Path
import csv
import json

input_path = Path("data") / 'input'
output_path = Path("data") / 'output'
input_path.mkdir(exist_ok=True, parents=True)
output_path.mkdir(exist_ok=True, parents=True)

sales_config_path = input_path / 'sales_config.json'
sales_csv_path = input_path / 'sales.csv'


def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: File not found -> {path}")
        return None


def load_sales(path):
    try:
        clean_sales = []

        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for sale in reader:
                clean_sale = {
                    "id": int(sale["id"]),
                    "product": sale["product"].strip(),
                    "category": sale["category"].strip().lower(),
                    "quantity": int(sale["quantity"]),
                    "unit_price": float(sale["unit_price"]),
                }

                clean_sales.append(clean_sale)

        return clean_sales

    except FileNotFoundError:
        print(f"Error: File not found -> {path}")
        return []


def build_sales_summary(sales, config):
    total_revenue_without_tax = 0
    sales_by_category = {}

    for sale in sales:
        sale_revenue = sale["quantity"] * sale["unit_price"]
        total_revenue_without_tax += sale_revenue

        category = sale["category"]

        if category not in sales_by_category:
            sales_by_category[category] = 0

        sales_by_category[category] += 1

    tax_rate = config["tax_rate"]
    total_tax = total_revenue_without_tax * tax_rate
    total_revenue_with_tax = total_revenue_without_tax + total_tax

    return {
        "report_name": config["report_name"],
        "currency": config["currency"],
        "total_sales": len(sales),
        "total_revenue_without_tax": round(total_revenue_without_tax, 2),
        "total_tax": round(total_tax, 2),
        "total_revenue_with_tax": round(total_revenue_with_tax, 2),
        "sales_by_category": sales_by_category,
    }


def export_summary(summary, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4, ensure_ascii=False)


config = load_config(sales_config_path)
sales = load_sales(sales_csv_path)
summary = build_sales_summary(sales, config)

print(config)
print(sales)
print(summary)

export_summary(summary, "data/output/sales_summary.json")
print("Sales summary exported")
