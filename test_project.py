import os
import csv
from project import calculate_total_with_tax, calculate_total, edit_item, create_tabulate

def create_temp_csv():
    with open("items.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Item", "Description",
                         "Unit Cost", "Quantity", "Line Total"])
        writer.writerow([1, "Laptop", "Powerful device", 1000.0, 2, 2000.0])
        writer.writerow([2, "Mouse", "Wireless", 50.0, 3, 150.0])

def test_calculate_total():
    create_temp_csv()
    assert calculate_total() == 2150.0
    os.remove("items.csv")

def test_calculate_total_with_tax():
    assert calculate_total_with_tax(100, 10) == 110
    assert calculate_total_with_tax(200, 0) == 200
    assert calculate_total_with_tax(0, 20) == 0

def test_create_tabulate():
    create_temp_csv()
    table = create_tabulate()
    # Just check that the output contains some expected strings
    assert "Laptop" in table
    assert "Mouse" in table
    os.remove("items.csv")
