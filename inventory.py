"""
Inventory Management System

This module provides functions to manage inventory including
adding items, removing items, checking quantities, and generating reports.
"""

import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add items to inventory with proper logging"""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        print(f"Error: Item name must be a string, got {type(item)}")
        return
    if not isinstance(qty, int) or qty < 0:
        print(f"Error: Quantity must be a positive integer, got {qty}")
        return

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove items from inventory with proper error handling"""
    try:
        if item not in stock_data:
            print(f"Error: {item} not found in inventory")
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: {item} not in inventory")
    except TypeError:
        print("Error: Invalid quantity type")


def get_qty(item):
    """Get quantity of an item safely"""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from file with proper error handling"""
    try:
        with open(file, "r", encoding="utf-8") as f:
            global stock_data # pylint: disable=global-statement
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        print(f"Error: {file} contains invalid JSON")


def save_data(file="inventory.json"):
    """Save inventory data to file with proper error handling"""
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(stock_data, indent=2))
    except IOError as e:
        print(f"Error saving data: {e}")


def print_data():
    """Print inventory report"""
    print("Items Report")
    print("-" * 30)
    if not stock_data:
        print("Inventory is empty")
        return
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("-" * 30)


def check_low_items(threshold=5):
    """Check for items below threshold"""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system"""
    print("Inventory Management System")
    print("=" * 30)

    # Valid operations
    add_item("apple", 10)
    add_item("orange", 15)
    add_item("banana", 8)

    # These will show validation errors
    add_item("banana", -2)  # Negative quantity - will be rejected
    add_item(123, 10)  # Invalid type - will be rejected

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"\nApple stock: {get_qty('apple')}")
    print(f"Banana stock: {get_qty('banana')}")
    print(f"Low items (below 5): {check_low_items()}")

    print("\n")
    print_data()

    save_data()
    print("\nData saved successfully")

    # Removed eval() for security
    print("Program completed successfully (eval removed for security)")


if __name__ == "__main__":
    main()
