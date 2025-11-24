# list comprehension

menu = ['espresso', 'latte', 'cappuccino', 'mocha', 'tea', 'frappe', 'hot chocolate', 'hot tea']

hot_drinks = [drink for drink in menu if 'hot' in drink]
print(hot_drinks)

# set comprehension
unique_lengths = {len(drink) for drink in menu}
print(unique_lengths)

recipes = {
    'espresso': ['water', 'coffee beans'],
    'latte': ['water', 'coffee beans', 'milk'],
    'cappuccino': ['water', 'coffee beans', 'milk', 'foam'],
    'mocha': ['water', 'coffee beans', 'milk', 'chocolate syrup'],
    'tea': ['water', 'tea leaves'],
    'frappe': ['ice', 'coffee beans', 'milk', 'sugar'],
    'hot chocolate': ['milk', 'chocolate syrup', 'whipped cream'],
    'hot tea': ['water', 'tea leaves', 'lemon']
}

unique_ingredients = {ingredient for ingredients in recipes.values() for ingredient in ingredients}
print(unique_ingredients) 

# dictionary comprehension
tea_prices_in_usd = {
    "matcha": 4.5,
    "black tea": 3.0,
    "green tea": 3.5,
    "earl grey": 4.0,
    "herbal tea": 4.5
}

tea_prices_in_inr = {tea: price * 80 for tea, price in tea_prices_in_usd.items()}
print(tea_prices_in_inr)

# generator comprehension
daily_sales = [150, 200, 250, 300, 350, 400, 450]
total_cups = sum(sale for sale in daily_sales if sale > 200)