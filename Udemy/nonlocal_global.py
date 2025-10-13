def update_order():
    order = {"type": "masala", "sugar": 2, "milk": 1, "quantity": 2}

    def add_sugar(amount):
        nonlocal order
        order["sugar"] += amount
        print(f"Added {amount} sugar. New sugar level: {order['sugar']}")
        print(f"Order sugar level: {order['sugar']}")

    def add_milk(amount):
        nonlocal order
        order["milk"] += amount
        print(f"Added {amount} milk. New milk level: {order['milk']}")

    add_sugar(1)
    add_milk(1)
    print(f"Final order: {order}")

update_order()

#global
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter value: {counter}")

increment_counter()