# Ticket Vending Machine App 
The Ticket Vending Machine App is a simple Python program designed to simulate a ticket vending machine at a department store. 

This app allows users to select products from different categories and generate tickets for those products. 

The app provides an interactive command-line interface for users to make their selections and obtain tickets.

# Features
Choose from a variety of product categories, including Perfume, Medicine, and Cosmetics.

Generate tickets for the selected products.

User-friendly interface with clear prompts and options.

Supports the generation of multiple tickets in a single session.

# How to Use
1. Download or copy the provided code into a Python file (e.g., ticket_vending_machine.py).

2. Open a terminal or command prompt and navigate to the directory where the Python file is located.

3. Run the app by executing the following command:

        python ticket_vending_machine.py

4. The app will display a welcome message and prompt you to select a product category.
You can choose from Perfume (P), Medicine (M), or Cosmetics (C) by entering the corresponding letter.

5. After selecting a product, the app will generate a ticket for that product.

6. The app will then ask if you would like to obtain another ticket. You can respond with Y (Yes) or N (No).

7. If you choose Y (Yes), the app will repeat the product selection and ticket generation process.

8. If you choose N (No), the app will display a goodbye message and terminate.

# Example
Here's an example interaction with the app:

    Welcome to the Department Store :
    [P] - Perfume
    [M] - Medicine
    [C] - Cosmetics
    Choose your product: P
    
    Your ticket number is : 
    P - 1
    Please wait for your turn :

    Would you like another ticket? - [Y] [N] - : Y
    [P] - Perfume
    [M] - Medicine
    [C] - Cosmetics
    Choose your product: M
    
    Your ticket number is : 
    M - 1
    Please wait for your turn : 

    Would you like another ticket? - [Y] [N] - : N
    Thanks for visiting the Department store. Goodbye.

# Note
The app uses the numbers module to call the decorate_ticket function, which is not provided in the code snippet.

Make sure to have the appropriate implementation of this function for the app to work correctly.

This app is designed as a simple simulation and does not handle real transactions or products. 

It's meant for educational purposes and as a demonstration of basic programming concepts.

# Author
This Ticket Vending Machine App was created by Chris Schinner.

Feel free to modify, expand, and enhance the app according to your needs. Enjoy!

