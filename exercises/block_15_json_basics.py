import json
from pathlib import Path


output_folder = Path("data") / "output"
customer_path = output_folder / "customer.json"
output_folder.mkdir(parents=True, exist_ok=True)
if output_folder.is_dir():
    customer = {
        "id": 101,
        "name": "Josué",
        "email": "josue@example.com",
        "is_active": True,
        "last_login": None,
        "roles": ["user", "admin"],
    }

    print(customer)
    print(type(customer))

    customer_json = json.dumps(customer)
    print(customer_json)
    print(type(customer_json))

    subscription_json = '{"plan": "premium", "price": 19.99, "active": true, "cancelled_at": null}'
    subscription = json.loads(subscription_json)

    print(subscription)
    print(type(subscription))
    print(subscription["active"])
    print(subscription["cancelled_at"])

    with open(customer_path, "w", encoding="utf-8") as file:
        json.dump(customer, file, indent=4, ensure_ascii=False)

    print("File written")

    with open(customer_path, "r", encoding="utf-8") as file:
        loaded_customer = json.load(file)

    print(loaded_customer)
    print(type(loaded_customer))
    print(loaded_customer["name"])
    print(loaded_customer["is_active"])
    print(loaded_customer["last_login"])

else:
    print("Output folder is not created")
