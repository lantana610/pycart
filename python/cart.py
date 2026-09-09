def add_item(item_name, price):
    cart.append({"item": item_name, "price": price})
    print("adding", item_name, "with price", price, "to the cart ...")
add_item("Apple", 2)
add_item("Bread", 3)
add_item("Milk", 4)

def view_cart():
    if len(cart) == 0:
        print("your cart is empty")
    else:
        for item in cart:
            print(item["item"], "_", item["price"])

def remove_item(item_name):
    found = False
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(item_name, "has been removed from the cart.")
            found = True
            break
    if not found:
        print(item_name, "was not found in cart.")
remove_item("milk")
view_cart()        