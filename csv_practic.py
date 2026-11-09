# csv_practice.py
#Author: Ashley Parker
# Module 12 Lab: Read a Sales CSV, Write a cleaned Report

#1 Python is better for automating large amounts of data and repeating tasks because it can read, transform, and write files quickly with code. Excel is easier for manually editing data, creating charts, and viewing information, but Python can automate processes that would take longer in Excel.
#2 A business could use an append-mode log file to track daily customer orders. Each new order would be added to the end of the file without deleting previous orders, making it easy to maintain a complete record of transactions.

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("--- Exercise 1 ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("--- Exercise 2 ---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--- Exercise 3 ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader) #next() returns next item from iterator
    print(f"header: {header}")
    for row in reader:
        print(row)

print("---exercise 4---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total_revenue += price * quantity
        print(f"{product}: {quantity} units x ${price:.2f} = ${price * quantity:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


print("---exercise 5---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rows_read += 1
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, price, quantity, total])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

print("---exercise 6---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total sales: ${dict_total:.2f}")

print("---exercise 7---")
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("---exercise 8---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
print(f"log entries so far: {entries}")













