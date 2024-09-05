# Project Collection

This repository contains several Python programs that perform various tasks.

## QR Code Generator

This program takes a user's name and phone number as input and generates a QR code containing that information.

### Usage
1. Run the program.
2. Enter your name when prompted.
3. Enter your phone number when prompted.
4. The program will generate a QR code file named `qrcode.png` containing your name and phone number.

### Requirements
- Python 3.x
- `qrcode` library (install using `pip install qrcode`)

### Example

Enter your name: John Doe
Enter your phone number: 1234567890
QR code generated successfully! Check the file 'qrcode.png'.


---

## Factorial Checker

This program checks whether a given number is a factorial or not. If the number is a factorial, it prints "yes"; otherwise, it prints "no".

### Usage
1. Run the program.
2. Enter a number when prompted.
3. The program will determine whether the number is a factorial and print the result.

### Example

Enter a number: 24
yes

In this example, 24 is a factorial because 24 = 4! (4 * 3 * 2 * 1).

---

## Instagram New Followers Finder

This program identifies new followers for a specified Instagram account. It compares the current followers with the previous list to find new additions.

### Usage
1. Run the program.
2. Enter your Instagram username and password when prompted.
3. Enter the target username to check for new followers.
4. The program will display the new followers, if any.

### Requirements
- Python 3.x
- `instaloader` library (install using `pip install instaloader`)

### Example

Enter your Instagram username: your_username
Enter your Instagram password: your_password
Enter the target username to check for new followers: target_username
New Followers:
new_follower1
new_follower2


---

## List Reverser

This program takes a list as input and reverses the order of its elements.

### Usage
1. Run the program.
2. Enter a list of elements separated by commas when prompted.
3. The program will display the original list and the reversed list.

### Example

Enter a list of elements separated by commas: 2, 3, 6, 1, 0, 14, 16, 7
Original List: [2, 3, 6, 1, 0, 14, 16, 7]
Reversed List: [7, 16, 14, 0, 1, 6, 3, 2]


---

## Duplicate Remover

This program takes a list as input and removes any duplicate elements from it.

### Usage
1. Run the program.
2. Enter a list of elements separated by commas when prompted.
3. The program will display the original list and the list with duplicates removed.

### Example

Enter a list of elements separated by commas: 2, 3, 6, 7, 7, 14, 2, 7
Original List: [2, 3, 6, 7, 7, 14, 2, 7]
List with Duplicates Removed: [3, 6, 14, 2, 7]
