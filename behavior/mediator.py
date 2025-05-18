class CartMediator:
    def __init__(self):
        self.product_selector = None
        self.quantity_field = None
        self.discount_applier = None
        self.total_display = None

    def notify(self, sender, event):
        if event == "product_selected":
            self.quantity_field.reset()
            self.update_total()
        elif event == "quantity_changed":
            self.update_total()
        elif event == "discount_applied":
            self.update_total()

    def update_total(self):
        price = self.product_selector.get_price()
        qty = self.quantity_field.get_quantity()
        discount = self.discount_applier.get_discount()
        total = (price * qty) * (1 - discount)
        self.total_display.show(total)
 
class ProductSelector:
    def __init__(self, mediator):
        self.mediator = mediator
        self.price = 100.0  # Simulated fixed price

    def select_product(self):
        print("📦 Product selected")
        self.mediator.notify(self, "product_selected")

    def get_price(self):
        return self.price


class QuantityField:
    def __init__(self, mediator):
        self.mediator = mediator
        self.qty = 1

    def set_quantity(self, qty):
        self.qty = qty
        print(f"🔢 Quantity set to {qty}")
        self.mediator.notify(self, "quantity_changed")

    def get_quantity(self):
        return self.qty

    def reset(self):
        print("🔄 Quantity reset to 1")
        self.qty = 1


class DiscountApplier:
    def __init__(self, mediator):
        self.mediator = mediator
        self.discount = 0.0

    def apply_discount(self, code):
        if code == "SAVE10":
            self.discount = 0.10
            print("🏷️ 10% discount applied")
        else:
            self.discount = 0.0
            print("❌ Invalid discount")
        self.mediator.notify(self, "discount_applied")

    def get_discount(self):
        return self.discount


class CartTotalDisplay:
    def show(self, total):
        print(f"🧾 Total: ${total:.2f}")

# Create mediator and components
mediator = CartMediator()
mediator.product_selector = ProductSelector(mediator)
mediator.quantity_field = QuantityField(mediator)
mediator.discount_applier = DiscountApplier(mediator)
mediator.total_display = CartTotalDisplay()

# Simulate user flow
mediator.product_selector.select_product()
mediator.quantity_field.set_quantity(3)
mediator.discount_applier.apply_discount("SAVE10")
