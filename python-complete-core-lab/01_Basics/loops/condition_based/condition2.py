# wap to check the present vegetables for customer and requested vegetables for customer
vegetables = ["onion", "pumpkin", "raddish", "carrot", "cucumber"]
order_vegetable = ["potato", "pumpkin", "carrot", "chilli"]

for vegetable in vegetables[0:3]:
    if vegetable in order_vegetable:
        print(f"your {vegetable} soup order is placed now pls wait for few hour")
    else:
        print(f"sorry' pls vist next time {vegetable} soup are not possible")


p_pizza = ["olives", "green peppers", "extra chees", "veg pizza"]
r_pizza = ["tommato", "olives", "peeper"]
for pizza in p_pizza[0:2]:
    if pizza in r_pizza:
        print(f"your {pizza} pizza is ready for breakfast")
    else:
        print(f"{pizza} pizza is not in p_pizza")

