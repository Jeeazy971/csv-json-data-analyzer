import csv
from pathlib import Path

input_folder = Path('data') / 'input'
output_folder = Path('data') / 'output'
product_path = input_folder / 'products.csv'
product_output_path = output_folder / 'clean_products.csv'

input_folder.mkdir(exist_ok=True, parents=True)
output_folder.mkdir(exist_ok=True, parents=True)


def load_clean_products(input_path):
    clean_products = []
    with open(input_path, 'r', encoding='utf-8', newline="") as file:
        products = csv.DictReader(file)

        for product in products:
            clean_product = {
                "id": int(product["id"]),
                "name": product["name"].strip(),
                "price": float(product["price"]),
                "category": product["category"].strip().lower(),
                "stock": int(product["stock"])
            }

            clean_products.append(clean_product)
    return clean_products


def count_products_by_category(products):
    category_counts = {}

    for product in products:
        category = product["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    return category_counts


def calculate_total_stock_value(products):
    total = 0
    for product in products:
        total += product["price"] * product["stock"]

    return total


def export_clean_products(products, output_path):
    with open(output_path, 'w', encoding="utf-8", newline="") as file:
        fieldnames = ["id", "name", "price", "category", "stock"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)


products = load_clean_products(product_path)

print(products)
print(count_products_by_category(products))
print(calculate_total_stock_value(products))

export_clean_products(products, product_output_path)
print("Clean CSV exported")
