def find_item_by_name(items, item_name):
    return next((i for i in items if item_name in i.name), None)
