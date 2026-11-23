import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for argument in sys.argv[1:]:
        try:
            item, quantity_text = argument.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item = item.strip()
        if not item:
            print(f"Error - invalid parameter '{argument}'")
            continue
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue
        if quantity < 0:
            print(f"Quantity error for '{item}': cannot be negative")
            continue

        inventory[item] = quantity

    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item in inventory:
        percentage = 0.0
        if total > 0:
            percentage = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {percentage}%")

    if items:
        most = items[0]
        least = items[0]
        for item in inventory:
            if inventory[item] > inventory[most]:
                most = item
            if inventory[item] < inventory[least]:
                least = item
        print(f"Item most abundant: {most} "
              f"with quantity {inventory[most]}")
        print(f"Item least abundant: {least} "
              f"with quantity {inventory[least]}")
    else:
        print("Inventory is empty; no most or least abundant item.")

    # inventory.update({"magic_item": 1})
    # print(f"Updated inventory: {inventory}")
    new_item = "magic_item"
    suffix = 1
    while new_item in inventory:
        new_item = f"magic_item_{suffix}"
        suffix += 1
    inventory.update({new_item: 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
