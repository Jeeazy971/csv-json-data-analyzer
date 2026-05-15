import csv
import json
from pathlib import Path

input_path = Path("data") / 'input'
input_path.mkdir(exist_ok=True, parents=True)
output_path = Path("data") / 'output'
output_path.mkdir(exist_ok=True, parents=True)
import_path = input_path / 'import_config.json'
missing_path = input_path / 'missing_config.json'
broken_path = input_path / 'broken_config.json'
import_summary = output_path / 'import_summary.json'
orders_with_errors = input_path / 'orders_with_errors.csv'


def load_json_config(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: file not found -> {path}")
        return None

    except json.JSONDecodeError:
        print(f"Invalid JSON content -> {path}")
        return None


def has_required_columns(reader, required_columns):
    if reader.fieldnames is None:
        return False

    return required_columns.issubset(reader.fieldnames)


def load_clean_orders(path):
    valid_orders = []
    invalid_rows = []

    required_columns = {"id", "customer", "total", "status"}

    try:
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            if not has_required_columns(reader, required_columns):
                print("Error: missing required CSV columns")
                return {
                    "valid_orders": [],
                    "invalid_rows": []
                }

            for row in reader:
                try:
                    clean_order = clean_order_row(row)
                    valid_orders.append(clean_order)

                except ValueError as error:
                    invalid_rows.append({
                        "row": row,
                        "error": str(error)
                    })

                except KeyError as error:
                    invalid_rows.append({
                        "row": row,
                        "error": f"Missing column: {error}"
                    })

    except FileNotFoundError:
        print(f"Error: CSV file not found -> {path}")

    return {
        "valid_orders": valid_orders,
        "invalid_rows": invalid_rows
    }


def clean_order_row(row):
    customer = row["customer"].strip()
    status = row["status"].strip().lower()

    if customer == "":
        raise ValueError("Customer is empty")

    if status == "":
        raise ValueError("Status is empty")

    return {
        "id": int(row["id"]),
        "customer": customer,
        "total": float(row["total"]),
        "status": status,
    }


def build_order_summary(valid_orders, invalid_rows):
    total_revenue = 0
    orders_by_status = {}

    for order in valid_orders:
        total_revenue += order["total"]

        status = order["status"]

        if status not in orders_by_status:
            orders_by_status[status] = 0

        orders_by_status[status] += 1

    return {
        "valid_orders": len(valid_orders),
        "invalid_rows": len(invalid_rows),
        "total_revenue": total_revenue,
        "orders_by_status": orders_by_status
    }


def export_summary(summary, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4, ensure_ascii=False)


config = load_json_config(import_path)
print(config)

missing_config = load_json_config(missing_path)
print(missing_config)

broken_config = load_json_config(broken_path)
print(broken_config)

result = load_clean_orders(orders_with_errors)

valid_orders = result["valid_orders"]
invalid_rows = result["invalid_rows"]

print(valid_orders)
print(invalid_rows)
print(len(invalid_rows))

summary = build_order_summary(valid_orders, invalid_rows)
print(summary)

export_summary(summary, import_summary)
print("Summary exported")
