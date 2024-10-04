import time 
import qrcode
PRODUCTS = []

def read_from_database():
    f = open('newproject/database.txt','r')
    
    for line in f:
        result = line.split(',')
        my_dict = {"code":result[0],'name':result[1],'price':result[2],'count':result[3]}
        PRODUCTS.append(my_dict)
    f.close() 
    

def show_menu():
    print('1- Add')    
    print('2- Edit')    
    print('3- Remove')    
    print('4- Search')    
    print('5- Show List')    
    print('6- Buy')    
    print('7- product detail QRcode')    
    print('8- Exit')    
      
def make_QRcode():
    user_choose = input('product id => ')
    for product in PRODUCTS:
        if user_choose == product['code']:
            img = qrcode.make(product)
            img.save('code.png')
def add():
    code = input('enter code => ')
    name = input('enter name => ')
    price = input('enter price => ')
    count = input('enter count => ')
    new_product = {'code':code,"name":name,"price":price,'count':count}
    PRODUCTS.append(new_product)
    print(PRODUCTS)
def edit():
    product_id = input("enter product id => ")
    for product in PRODUCTS:
        if product['code'] == product_id:
            product_edit = int(input('edit name => 1 \t edit price => 2 \t edit count => 3 '))
            if product_edit == 1:
                edit_name = input('write new name ')
                finally_name = product["name"] = edit_name
                PRODUCTS.append(finally_name)
                print("name edited successfully")
                break
            elif product_edit == 2:
                edit_price = int(input('enter new price '))
                finally_price = product['price'] = edit_price
                PRODUCTS.append(finally_price)
                print("price edited successfully")
                break
            elif product_edit == 3:
                edit_count = int(input('enter new count '))
                finally_count = product['count'] = edit_count
                PRODUCTS.append(finally_count)
                print("count edited successfully")
                break
            else:
                print('invalid value')
        else:
            print('not found')
    else:
        
        print("invalid input")        
def remove():
    product_delete = input("product id => ")
    for product in PRODUCTS:
        if product["code"] == product_delete:
            PRODUCTS.remove(product)
            print(f"Product with ID {product_delete} has been removed.")
            break
        else:
            print(f'product with this id => {product_delete} not found') 
def search():
    user_input = input("type your keyword => ")
    for product in PRODUCTS:
       if product['code'] == user_input or product['name'] == user_input: 
        print(product['code'], '\t' , product['name'], '\t' , product["price"], '\t')
        break
    else:
           print('not found')
    
def show_list():
    print("code\tname\tprice")
    for product in PRODUCTS:
        print(product['code'], '\t' , product['name'], '\t' , product["price"], '\t')

def buy():
    ...
    
def set_to_database():
    ...

print('welcome my store')
time.sleep(0.5)
print('Loading.') 
time.sleep(0.5)
print('Loading..') 
time.sleep(0.5)
print('Loading...') 
time.sleep(0.5)
read_from_database()
print('data Loaded')
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