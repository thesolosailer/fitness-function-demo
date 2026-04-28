import inventory_service

def place_order(item_id, quantity):
    inventory_service.reserve_stock(item_id, quantity)
    print(f"Order placed for {quantity} of {item_id}")
