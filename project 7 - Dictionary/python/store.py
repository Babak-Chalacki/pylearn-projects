import time 
import qrcode

PRODUCTS = []

def read_from_database():
    f = open('database.txt', 'r')
    
    for line in f:
        result = line.strip().split(',')
        my_dict = {"code": result[0], 'name': result[1], 'price': float(result[2]), 'count': int(result[3])}
        PRODUCTS.append(my_dict)
    f.close() 

def show_menu():
    print('1- Add')    
    print('2- Edit')    
    print('3- Remove')    
    print('4- Search')    
    print('5- Show List')    
    print('6- Buy')    
    print('7- Product Detail QRcode')    
    print('8- Save to Database')    
    print('9- Exit')    

def make_QRcode():
    user_choose = input('Product ID => ')
    for product in PRODUCTS:
        if user_choose == product['code']:
            img = qrcode.make(product)
            img.save('code.png')
            print("QR code generated and saved as 'code.png'.")
            return
    print("Product not found.")

def add():
    code = input('Enter code => ')
    name = input('Enter name => ')
    price = float(input('Enter price => '))
    count = int(input('Enter count => '))
    new_product = {'code': code, "name": name, "price": price, 'count': count}
    PRODUCTS.append(new_product)
    print("Product added successfully.")

def edit():
    product_id = input("Enter product ID => ")
    for product in PRODUCTS:
        if product['code'] == product_id:
            product_edit = int(input('Edit name => 1 \t Edit price => 2 \t Edit count => 3 '))
            if product_edit == 1:
                edit_name = input('Write new name: ')
                product["name"] = edit_name
                print("Name edited successfully.")
                break
            elif product_edit == 2:
                edit_price = float(input('Enter new price: '))
                product['price'] = edit_price
                print("Price edited successfully.")
                break
            elif product_edit == 3:
                edit_count = int(input('Enter new count: '))
                product['count'] = edit_count
                print("Count edited successfully.")
                break
            else:
                print('Invalid value')
            return
    print("Product not found.")

def remove():
    product_delete = input("Product ID => ")
    for product in PRODUCTS:
        if product["code"] == product_delete:
            PRODUCTS.remove(product)
            print(f"Product with ID {product_delete} has been removed.")
            return
    print(f'Product with this ID => {product_delete} not found.') 

def search():
    user_input = input("Type your keyword => ")
    for product in PRODUCTS:
       if product['code'] == user_input or product['name'] == user_input: 
           print(product['code'], '\t', product['name'], '\t', product["price"], '\t', product["count"])
           return
    print('Not found')

def show_list():
    print("Code\tName\tPrice\tCount")
    for product in PRODUCTS:
        print(product['code'], '\t', product['name'], '\t', product['price'], '\t', product['count'])

def buy():
    user_input = input("Enter the Product ID you want to buy: ")
    quantity = int(input("Enter quantity: "))
    
    for product in PRODUCTS:
        if product['code'] == user_input:
            if quantity <= product['count']:
                total_cost = quantity * product['price']
                product['count'] -= quantity
                print(f"You bought {quantity} of {product['name']} for ${total_cost:.2f}.")
                
                if product['count'] == 0:
                    remove() 
                return
            else:
                print(f"Insufficient stock. Available count is {product['count']}.")
                return
    print("Product not found.")

def set_to_database():
    with open('database.txt', 'w') as f:
        for product in PRODUCTS:
            f.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
    print("Data saved to database.")

print('Welcome to my store')
time.sleep(0.5)
print('Loading.') 
time.sleep(0.5)
print('Loading..') 
time.sleep(0.5)
print('Loading...') 
time.sleep(0.5)
read_from_database()
print('Data Loaded')

while True:
    show_menu()
    
    user_input = input('What is your choice => ')
    
    try:
        choice = int(user_input)
        
        if choice == 1:
            add()
        elif choice == 2:
            edit()
        elif choice == 3:
            remove()
        elif choice == 4:
            search()
        elif choice == 5:
            show_list()
        elif choice == 6:
            buy()
        elif choice == 7:
            make_QRcode()
        elif choice == 8:
            set_to_database()
        elif choice == 9:
            print("Exiting program.")
            exit(0)
        else:
            print("Invalid number, please try again.")
    
    except ValueError:
        print("Please enter a valid number.")