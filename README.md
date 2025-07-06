# InvoiceCraft


#### Description:
**InvoiceCraft** is a Python-based invoicing tool developed as a final project for **CS50’s Introduction to Programming with Python**. It allows users to easily create, manage, and export professional invoices in PDF format.

- Add, edit, invoice items
- Calculate totals with tax
- Display items in a formatted table
- Add stamp on PDF
- Export the final invoice as a PDF

The project is built using standard Python libraries and a few third-party packages like `tabulate` for clean display and `fpdf` for generating PDFs.

---

## Features:

### 🔧 Add, Edit, and Manage Invoice Items

Users can input multiple items with descriptions, unit costs, and quantities.
Each item can be edited individually even after entry.

### 📊 Automatic Calculations

The application automatically calculates line totals for each item and provides a net total.
Users can also apply a custom tax rate to calculate the final amount.

### 📋 Formatted Table Display
All entered items are displayed in a clean, organized table using the `tabulate` library,
making it easy to review before export.

### 🖋️ Stamp Integration on PDF

A stamp image (`stamp.png`) is added automatically to the final PDF for added professionalism.
(Optional signature feature included.)

### 📄 PDF Invoice Export

Generates a professional-looking invoice in PDF format using the `fpdf` library.
The invoice includes company and client info, a detailed product list, totals, tax, and visual branding.


## How to Run

1. Clone or download this project repository
2. **Install the required dependencies** by this commande: `pip install -r requirements.txt`
3. Run the project by executing: `python project.py`


## File Structure

InvoiceCraft/
├── project.py -- The main program file containing the application logic.
├── test_project.py -- Unit tests for your functions.
├── requirements.txt -- List of Python libraries required to run the project.
├── stamp.png -- The stamp image used on the PDF invoice.
└── items.csv -- Temporary CSV file used to store item data (deleted automatically after PDF generation).


## Technologies Used

- Python 3.x
- [tabulate](https://pypi.org/project/tabulate/) — For displaying data in formatted tables.
- [fpdf](https://pyfpdf.github.io/fpdf2/) — To generate PDF files.
- [pyfiglet](https://pypi.org/project/pyfiglet/) — For fancy ASCII art text in the terminal.


## How to Use

1. Run the program
   After installing dependencies, start the program by running:
   `python project.py`
   You will see a welcome message: "Welcome to Craft Invoice".

2. Start creating a new invoice
   When prompted, type y to start or n to exit the program.

3. Enter company information
   You will be asked to provide:
   - Company Name
   - Tax Identification Number (TIN)
   - Business Registration Number
   - Company Address
   - Phone Number
   - Email Address

4. Enter client information
   Similarly, provide details for the client:
   - Client Name
   - Client Address
   - Phone Number
   - Email Address

5. Add invoice items
   For each item, enter:
   - Item Name
   - Description
   - Unit Cost (decimal number)
   - Quantity (integer)

   You can add as many items as needed. To finish adding items, press Ctrl + D (on Linux/macOS) or Ctrl + Z then Enter (on Windows).

6. View items in a formatted table
   Once you finish entering items, the program displays all items in a clear, organized table.

7. Edit items if needed
   The program will ask if you want to edit any item. If yes, you can select which item and which attribute (name, description, unit cost, quantity) to update.
   You can repeat editing until you confirm you are done.

8. Enter tax percentage
   Input the tax rate (%) to apply to the invoice total.

9. Invoice generation
   The program calculates the total, adds the tax, and generates a PDF invoice file.
   The PDF includes company and client info, a detailed list of items, totals, tax amounts, and adds a professional stamp image.

10. Completion
    The generated PDF file will be saved in the project folder with a name like:
    invoice_clientname_YYYY_MM_DD.pdf



## Testing

This project includes automated tests using `pytest` to ensure core functions work as expected.
Tests cover functions such as:

- `calculate_total()` – sums all line totals from invoice items.
- `calculate_total_with_tax(total, tax)` – computes total amount including tax.
- `create_tabulate()` – generates a formatted table of invoice items.

You can run the tests by executing: `pytest test_project.py`


---

## Author Information

- **Name:** Hamza Serhani
- **GitHub Username:** https://github.com/Hamser1001
- **edX Username:** upscale_mind50
- **Location:** Agadir, Morocco
- **Date of Recording:** 03-07-2025

## Acknowledgments
Special thanks to CS50
