import json

product = {
    "id": 1,
    "name": "Laptop",
    "price": 899.99,
    "available": True,
    "discount": None,
    "tags": ["computer", "tech"],
}

print(product)
print(type(product))

product_json = json.dumps(product)

print(product_json)
print(type(product_json))

order_json = '{"id": 10, "customer": "Alice", "paid": true, "delivery_date": null}'

order = json.loads(order_json)

print(order)
print(type(order))
print(order["paid"])
print(order["delivery_date"])
