# You’ll build a system where:
# 	•	A user can choose a pizza.
# 	•	Decorators will:
# 	    •	add logging 🍕
# 	    •	track time ⏱️
# 	    •	apply discounts 💸
# 	•	Lambdas will:
# 	    •	calculate prices with toppings
# 	    •	format the receipt


menu = {
    "paneer" : 20,
    "triplecheese" : 23,
    "corn" : 12
}

extra_cheese = lambda x: x+2
stuffed_crust = lambda x: x+3

def order_pizza(pizza, *toppings):
    if pizza not in menu:
        raise ValueError("Pizza not on the menu!")
    base_price = menu[pizza]
    for topping in toppings:
        base_price = topping(base_price)
    return base_price

if __name__ == "__main__":
    total = order_pizza("paneer", extra_cheese, stuffed_crust)
    print("Pay: $",total)