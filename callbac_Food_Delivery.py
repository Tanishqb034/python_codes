def order_ready():
    print("Your order is ready for pickup!")

def prepare_food(callback):
    print("Preparing food...")
    print("Cooking...")
    callback()

prepare_food(order_ready)