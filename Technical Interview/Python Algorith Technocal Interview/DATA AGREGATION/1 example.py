# Sample data - list of transactions
transactions = [
    {"product": "A", "amount": 50},
    {"product": "B", "amount": 30},
    {"product": "A", "amount": 20},
    {"product": "C", "amount": 40},
    {"product": "B", "amount": 60},
    {"product": "C", "amount": 10},
]

# Initialize an empty dictionary to store aggregated results
aggregated_data = {}

# Aggregate data
for transaction in transactions:
    product = transaction["product"]
    amount = transaction["amount"]

    # If the product is not in the dictionary, add it with the current amount
    if product not in aggregated_data:
        aggregated_data[product] = amount
    else:
        # If the product is already in the dictionary, update the total amount
        aggregated_data[product] += amount

# Print the aggregated data
for product, total_amount in aggregated_data.items():
    print(f"Product: {product}, Total Sales: {total_amount}")
