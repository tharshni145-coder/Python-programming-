import os

print("=== STORE CHECKOUT SYSTEM ===\n")

# --- 1. ValueError & TypeError ---
# Scenario: Converting user text input to an integer or mixing incompatible types
try:
    raw_quantity = input("Enter item quantity to purchase: ")
    quantity = int(raw_quantity)  # Raises ValueError if input is not a number

    # total_price = "10.0" + 5    # Would raise TypeError (un-comment to test)
    total_price = quantity * 10.0
    print(f"Subtotal for {quantity} items: ${total_price:.2f}\n")

except ValueError:
    print("❌ ValueError: Invalid input! Quantity must be a whole number.\n")
    quantity = 0  # Default value so the rest of the script doesn't crash
except TypeError:
    print("❌ TypeError: Cannot combine incompatible data types.\n")
    quantity = 0


# --- 2. ZeroDivisionError ---
# Scenario: Splitting a fixed discount across items when quantity is 0
try:
    discount = 50.0
    discount_per_item = discount / quantity  # Raises ZeroDivisionError if quantity == 0
    print(f"Discount applied per item: ${discount_per_item:.2f}\n")

except ZeroDivisionError:
    print("❌ ZeroDivisionError: Cannot split a discount across 0 items!\n")


# --- 3. IndexError ---
# Scenario: Accessing a list element with an out-of-bounds index
promo_gifts = ["Keychain", "Sticker", "Tote Bag"]
try:
    choice_index = int(input("Pick a promo gift index (0, 1, or 2): "))
    selected_gift = promo_gifts[choice_index]  # Raises IndexError if index is 3 or higher
    print(f"You selected: {selected_gift}\n")

except IndexError:
    print("❌ IndexError: Invalid choice! That item index does not exist in the list.\n")
except ValueError:
    print("❌ ValueError: Gift index must be a valid number.\n")


# --- 4. PermissionError ---
# Scenario: Attempting to save a file in a restricted system folder
try:
    # Trying to open a system file location that lacks user write permissions
    with open("/system_receipt_test.txt", "w") as file:
        file.write("Receipt Data")

except PermissionError:
    print("❌ PermissionError: Access denied! Cannot write to a protected directory.\n")


# --- 5. NameError ---
# Scenario: Calling a variable that was never declared or misspelled
try:
    # 'receipt_id' was never defined above
    print(f"Receipt ID: {receipt_id}\n")

except NameError:
    print("❌ NameError: Variable 'receipt_id' is not defined anywhere in the script.\n")

print("=== Checkout Process Finished ===")