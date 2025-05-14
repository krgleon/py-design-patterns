# First decorator: adds validation logic.
# This is a "concrete decorator" that wraps the base function and adds a new responsibility (input validation).
def validate_payment(func):
    def wrapper(amount):
        if amount <= 0:
            print("❌ Invalid payment amount!")
            return
        # Delegates to the next layer (original function or another decorator)
        return func(amount)
    return wrapper

# Second decorator: adds logging.
# Another "concrete decorator" that wraps a function and adds logging functionality before delegating.
def log_payment(func):
    def wrapper(amount):
        print(f"📜 LOG: Payment attempt of ${amount}")
        return func(amount)
    return wrapper

# Here we apply the decorators using the @ syntax.
# log_payment wraps validate_payment, which wraps process_payment.
# This shows how the Decorator pattern allows multiple behaviors to be layered dynamically.
@log_payment
@validate_payment
def process_payment(x):
    print(f"💰 Processing payment of ${x}")

# The client code calls the function as usual.
# The decorators add functionality transparently, which is the essence of the pattern.
process_payment(100)    # Valid case triggers all layers
process_payment(-50)    # Fails validation, skips base function
