class OrderService:
    def __init__(self, inventory_service):
        self.inventory_service = inventory_service

    def place_order(self, item_id, quantity):
        self.inventory_service.reserve_stock(item_id, quantity)
        print(f"Order placed for {quantity} of {item_id}")
