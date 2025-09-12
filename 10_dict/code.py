chai_order = dict(type="masala", sugar=2, milk=1, quantity=2)
print(f"Chai order:", chai_order)
print(f"Chai type:", chai_order["type"])
print(f"Chai sugar:", chai_order["sugar"])

chai_order["sugar"] = 3
print(f"Chai sugar after update:", chai_order["sugar"])

chai_order["temperature"] = "hot"
print(f"Chai order after adding temperature:", chai_order)
print(f"Chai order keys:", chai_order.keys())
print(f"Chai order values:", chai_order.values())
print(f"Chai order items:", chai_order.items())

del chai_order["milk"]
print(f"Chai order after deleting milk:", chai_order)

#membership test
print(f"Is 'sugar' in chai_order?", 'sugar' in chai_order)

last_item = chai_order.popitem()
print(f"Popped item:", last_item)
print(f"Chai order after popping an item:", chai_order)

#update
chai_order.update({"sugar": 4})
print(f"Chai order after updating sugar:", chai_order)

#retrieve
sugar_amount = chai_order.get("sugar", 0)
customer_name = chai_order.get("customer_name", "Guest") #not use: customer_name = chai_order["customer_name"]