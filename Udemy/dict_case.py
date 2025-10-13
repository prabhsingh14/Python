users = [
    {"id": 1, "total": 100, "coupon": "P50"},
    {"id": 2, "total": 200, "coupon": "F30"},
    {"id": 3, "total": 300, "coupon": "P20"},
]

discounts = {
    "P50": (0, 10),
    "F30": (0.3, 0),
    "P20": (0.2, 0),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"User {user['id']} has a discount of {discount}")