def allocate_inventory(order, warehouses):
    # first, count the number of orders s.t. # order > 0
    order_length = 0
    for item, nums in order.items():
        if nums > 0:
            order_length += 1

    answer = []
    fulfilled = 0

    for warehouse in warehouses:
        # if order is fulfilled, there's no need to continue traversal
        if fulfilled >= order_length:
            break
        name = warehouse["name"]
        inventory = warehouse["inventory"]
        order_from_current_inventory = {name: {}}
        for item in inventory:
            # first check if item is in current order / greater than zero
            if item not in order or order[item] <= 0:
                continue
            # update order_from_current_inventory accordingly
            order_from_current_inventory[name][item] = (
                order[item] if order[item] < inventory[item] else inventory[item]
            )
            # subtract inventory amount from order amount
            order[item] -= inventory[item]
            # if order amount is l.t.e. zero, increment fulfilled
            if order[item] <= 0:
                fulfilled += 1
        # if order_from_current_inventory exists, add it to our global answer
        if len(order_from_current_inventory[name]):
            answer.append(order_from_current_inventory)

    # order is fulfilled if and only if fulfilled >= order_length
    return answer if fulfilled >= order_length else []