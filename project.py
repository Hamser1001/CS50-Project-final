import csv
from tabulate import tabulate
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime
from pyfiglet import Figlet
import sys
import os


class Item:
    def __init__(self, name, description, unit_cost, quantity):
        self.name = name
        self.description = description
        self.unit_cost = float(unit_cost)
        self.quantity = int(quantity)

    @property
    def line_total(self):
        return self.unit_cost * self.quantity


class Company:
    def __init__(self, company_name, tin, business_registration_number, company_address, number_phone, company_email):
        self.company_name = company_name
        self.tin = tin
        self.business_registration_number = business_registration_number
        self.company_address = company_address
        self.number_phone = number_phone
        self.company_email = company_email

    def __str__(self):
        return (
            f"Company Information\n"
            f"Company Name: {self.company_name}\n"
            f"Tax Identification Number: {self.tin}\n"
            f"Business Registration Number: {self.business_registration_number}\n"
            f"Company Address: {self.company_address}\n"
            f"Phone Number: {self.number_phone}\n"
            f"Email: {self.company_email}\n"
        )


class Client:
    def __init__(self, client_name, client_address, number_phone, client_email):
        self.client_name = client_name
        self.client_address = client_address
        self.number_phone = number_phone
        self.client_email = client_email

    def __str__(self):
        return (
            f"Client Information\n"
            f"Client Name: {self.client_name}\n"
            f"Client Address: {self.client_address}\n"
            f"Number Phone: {self.number_phone}\n"
            f"Email: {self.client_email}\n"
        )


def get_info_company():
    print("\n==== Company Information ====\n")

    # Get Company info
    try:
        company_name = input("Company Name: ").strip().title()
        tin = input("Tax Identification Number: ").strip()
        business_registration_number = input(
            "Business Registration Number: ").strip()
        company_address = input("Company Address: ").strip().capitalize()
        number_phone = input("Number Phone: ").strip()
        company_email = input("Email: ").strip().lower()

    except (EOFError, UnboundLocalError, KeyboardInterrupt):
        print("\nProgram is stopped!.\n\n")
        sys.exit(1)

    return Company(company_name, tin, business_registration_number, company_address, number_phone, company_email)


def get_info_client():
    print("\n==== Client Information ====\n")

    # Get Client information
    try:
        client_name = input("Client Name: ").strip().title()
        client_address = input("Client Address: ").strip().capitalize()
        number_phone = input("Number Phone: ")
        client_email = input("Email: ").strip().lower()

    except (EOFError, UnboundLocalError, KeyboardInterrupt):
        print("\nProgram is stopped!.\n\n")
        sys.exit(1)

    return Client(client_name, client_address, number_phone, client_email)


def get_items():

    # Create header for csv file
    with open('items.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Number', 'Item', 'Description', 'Unit Cost', 'Quantity', 'Line Total'])

        # Initilize Item numbering
        number = 0
    while True:
        try:
            # Item numbering
            number += 1

            # Get item
            print("\nEnter item details. Press Ctrl + D when you're done.\n")

            name = input(f"Item {number}: ").strip().title()
            description = input("Description: ").strip().capitalize()

            unit_cost = float(input("Unit Cost: ").strip())
            quantity = int(input("Quantity: ").strip())

            # Save Data in csv file
            with open('items.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                # Create a Item Object
                item = Item(name, description, unit_cost, quantity)

                # Create a item content each row with line total (unit cost * quantity)
                writer.writerow(
                    [number, item.name, item.description, item.unit_cost, item.quantity, item.line_total])

        except EOFError:

            print("\nFinished entering items.\n\n")
            break
        except ValueError:
            number -= 1
            print("Invalid input. Please enter numbers for cost and quantity.")
            continue


def edit_item():
    item_number = int(input("Enter number of item you want to edit: "))
    display_tabulate()
    # Choosing what item you want to edit
    print(
        "\n\n1.Edit Item\n2.Edit Description\n3.Edit Unit Cost\n4.Edit Quantity\n\n")
    choice = int(input("Enter a Number: "))

    # Open file for edit
    with open("items.csv", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    header = data[0]
    rows = data[1:]

    updated = False
    # On depends of choice, Edit
    for row in rows:
        if int(row[0]) == item_number:
            if choice == 1:
                new_name = input("Enter new Item name: ").title()
                row[1] = new_name
                updated = True
                print("Item name updated successfully.\n")
            elif choice == 2:
                new_description = input(
                    "Enter new Item description: ").capitalize()
                row[2] = new_description
                updated = True
                print("Item description updated successfully.\n")
            elif choice == 3:
                new_unit_cost = float(input("Enter new Item Unit Cost: "))
                row[3] = new_unit_cost
                row[5] = str(float(row[3]) * int(row[4]))
                updated = True
                print("Item Unit Cost updated successfully.\n")
            elif choice == 4:
                new_quantity = int(input("Enter new Item Quantity: "))
                row[4] = new_quantity
                row[5] = str(float(row[3]) * int(row[4]))
                updated = True
                print("Item Quantity updated successfully.\n")
            else:
                print("Number choice is not found\n")
            break

    # Update csv file
    if updated:
        with open("items.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
    else:
        print("Item number not found")


def create_tabulate():
    with open('items.csv', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    header = data[0]
    rows = data[1:]

    # Return a table
    return tabulate(rows, header, tablefmt='grid')


def display_tabulate():

    # Display a table
    print(create_tabulate())
    print()


def calculate_total():
    total = 0
    # Open the file to sum all line totals
    with open("items.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[5])
    return total


def calculate_total_with_tax(total, tax):
    return total + (total * tax) / 100


def generate_invoice_pdf(company, client, items, tax, total):

    # Font
    font = "Courier"

    # Create a pdf file and add page
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Inovice Title
    pdf.set_font(font, size=12)
    pdf.cell(0, 4, "Invoice", align="C")
    pdf.ln(12)

    # Date
    str_date = datetime.now().strftime("%Y-%m-%d")
    date = f'Date: {str_date}'

    pdf.set_font(font, size=9)
    pdf.cell(0, 4, str(date))
    pdf.ln(10)

    # Convert text as lines
    company_lines = str(company).strip().split("\n")
    client_lines = str(client).strip().split("\n")

    # Check if they had same lines length
    max_lines = max(len(company_lines), len(client_lines))

    while len(company_lines) < max_lines:
        company_lines.append("")
    while len(client_lines) < max_lines:
        client_lines.append("")

    # Set fonts and lines
    pdf.set_font(font, size=9)

    # Print lines
    for i in range(max_lines):
        pdf.cell(0, 4,
                 company_lines[i], border=0, new_x=XPos.RIGHT, new_y=YPos.TOP, align="L")
        pdf.cell(0, 4,
                 client_lines[i], border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
    pdf.ln(14)

    # Table Title
    pdf.set_font(font, size=10)
    pdf.cell(0, 4, "Products List", align="C")

    # Items table
    pdf.ln(8)
    pdf.set_font(font, size=9)
    pdf.multi_cell(0, 4, items)

    # Total and Tax
    pdf.ln(14)
    pdf.set_font(font, size=9)
    pdf.cell(0, 4, f"Net: {total}", new_x=XPos.LMARGIN,
             new_y=YPos.NEXT, align="R")
    pdf.cell(0, 4, f"Tax {tax}%: {total * tax / 100}", new_x=XPos.LMARGIN,
             new_y=YPos.NEXT, align="R")

    pdf.cell(
        0, 4, f"Total: {calculate_total_with_tax(total, tax)} MAD", new_x=XPos.LMARGIN,
        new_y=YPos.NEXT, align="R")
    pdf.ln(10)

    add_stamp_signature(pdf)

    # Save PDF
    pdf.output(
        f"invoice_{client.client_name.lower().replace(' ', '_')}_{str_date.replace('-', '_')}.pdf")
    os.remove("items.csv")


def add_stamp_signature(pdf):
    try:
        pdf.image("stamp.png", x=160, y=160, w=30, h=30)
        # pdf.image("signature.png", x=145, y=175, w=40)

    except RuntimeError:
        print("The stamp image could not be pdf loaded.\nMake sure the file exists and has the correct PNG extension.")


def main():

    # Welcome txt
    f = Figlet(font='larry3d')
    print(f.renderText('Welcome to Craft Invoice'))

    while True:
        start = input("Start create invoice (y/n): ").lower()
        if start == "y":

            # get information from user
            company = get_info_company()
            client = get_info_client()
            get_items()
            items = create_tabulate()
            display_tabulate()
            while True:
                try:
                    edit = input("\n\nYou want to Edit Item Details? (y/n):")
                    if edit == "y":
                        edit_item()
                        items = create_tabulate()
                        display_tabulate()
                    elif edit == "n":
                        break
                    else:
                        print("Invalid input!")
                        continue
                except ValueError:
                    print("Invalid input!")
                    continue

            total = calculate_total()
            print(f"Net: {total}")
            tax = int(input("Enter the tax: "))
            print(f"Total: {calculate_total_with_tax(total, tax)}")
            generate_invoice_pdf(company, client, items, tax, total)
            print("\nPdf generated\n\n")
            sys.exit(0)
        elif start == "n":
            print("\nProgram is stopped!.\n\n")
            sys.exit(1)
        else:
            print("Invalid input!")
            continue


if __name__ == "__main__":
    main()

"""
Number,Name,Description,Unit Cost,Quantity
1,Laptop,High-performance laptop,1200.50,2
2,Mouse,Wireless mouse,25.99,5
3,Keyboard,Mechanical keyboard,75.00,3
"""
