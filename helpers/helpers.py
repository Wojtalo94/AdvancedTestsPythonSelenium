def find_item_in_cart_by_name(items, item_name):
    return next((i for i in items if item_name in i.cart_item_name), None)


def find_item_in_store_by_name(items, item_name):
    return next((i for i in items if item_name in i.store_item_name), None)
