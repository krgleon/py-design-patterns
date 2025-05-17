# Subsystem service: handles inventory checking
class InventoryService:
    def check_stock(self, item_id):
        print(f"Checking stock for item {item_id}")
        return True  # Simulates that the item is in stock

# Subsystem service: handles payment processing
class PaymentService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        return True  # Simulates successful payment

# Subsystem service: handles invoice generation
class InvoiceService:
    def generate_invoice(self, item_id, amount):
        print(f"Generating invoice for item {item_id} - Amount: ${amount}")

# Subsystem service: handles user notifications
class NotificationService:
    def send_confirmation(self, item_id):
        print(f"Sending confirmation for item {item_id}")

# Facade class: provides a unified interface to interact with all subsystems
class OrderFacade:
    def __init__(self):
        # Internally instantiates all the subsystem services
        self.inventory = InventoryService()
        self.payment = PaymentService()
        self.invoice = InvoiceService()
        self.notification = NotificationService()

    # High-level method for clients to place an order without knowing subsystem details
    def place_order(self, item_id, amount):
        print("➡️ Starting order placement process...")

        # Delegates to the inventory service
        if not self.inventory.check_stock(item_id):
            print("❌ Item out of stock")
            return

        # Delegates to the payment service
        if not self.payment.process_payment(amount):
            print("❌ Payment failed")
            return

        # Delegates to the invoice service
        self.invoice.generate_invoice(item_id, amount)

        # Delegates to the notification service
        self.notification.send_confirmation(item_id)

        # Final success message from the facade
        print("✅ Order completed successfully")

# Client code: uses the facade instead of dealing with each subsystem individually
facade = OrderFacade()
facade.place_order(item_id=42, amount=150)
