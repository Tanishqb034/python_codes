def payment_success():
    print("Payment Successful!")
    print("Order Confirmed")

def process_payment(amount, callback):
    print(f"Processing payment of ₹{amount}...")
    
    # Payment completed
    callback()

process_payment(500, payment_success)