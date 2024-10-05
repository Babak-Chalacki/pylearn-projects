# project 7 - Store Management System

## Overview

This project is a Store Management System developed in Python. It allows users to manage products in a store, including editing product information, deleting products, purchasing items, and saving data to a file upon exit.

## Features

1. **Edit Product Information**:
   - Users can update the following fields of a product:
     - Name
     - Price
     - Count
   - A success message is displayed after the update.

2. **Delete Product**:
   - Users can delete a product by entering its code.
   - A confirmation message is shown upon successful deletion.

3. **Generate QR Code**:
   - A function that takes the product code and saves the product information as a QR code.

4. **Purchase from Store**:
   - Users can enter the product code to check if it exists.
     - If not found, an appropriate message is displayed.
   - If the product exists, users are prompted to enter the desired quantity.
     - If stock is insufficient, a warning message is shown.
     - If stock is sufficient, the inventory is updated and the item is added to the user's cart.
   - The purchase process continues until the user decides to stop.
   - A final invoice is printed, including each item's price and the total amount.

5. **Data Persistence**:
   - All data is saved to a file when the program exits to ensure information is not lost.

