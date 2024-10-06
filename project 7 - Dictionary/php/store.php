<?php


$PRODUCTS = [];

function read_from_database() {
    global $PRODUCTS;
    if (file_exists('database.txt')) {
        $file = fopen('database.txt', 'r');
        while (($line = fgets($file)) !== false) {
            $result = explode(',', trim($line));
            $PRODUCTS[] = [
                "code" => $result[0],
                "name" => $result[1],
                "price" => floatval($result[2]),
                "count" => intval($result[3])
            ];
        }
        fclose($file);
    }
}

function show_menu() {
    echo "\n1- Add\n";
    echo "2- Edit\n";
    echo "3- Remove\n";
    echo "4- Search\n";
    echo "5- Show List\n";
    echo "6- Buy\n";
    echo "7- Product Detail QRcode\n";
    echo "8- Save to Database\n";
    echo "9- Exit\n";
}

function add() {
    global $PRODUCTS;
    
    $code = readline('Enter code => ');
    $name = readline('Enter name => ');
    $price = floatval(readline('Enter price => '));
    $count = intval(readline('Enter count => '));
    
    $PRODUCTS[] = [
        'code' => $code,
        'name' => $name,
        'price' => $price,
        'count' => $count
    ];
    
    echo "Product added successfully.\n";
}

function edit() {
    global $PRODUCTS;
    
    $product_id = readline("Enter product ID => ");
    
    foreach ($PRODUCTS as &$product) {
        if ($product['code'] == $product_id) {
            $product_edit = intval(readline('Edit name => 1, Edit price => 2, Edit count => 3: '));
            switch ($product_edit) {
                case 1:
                    $edit_name = readline('Write new name: ');
                    $product["name"] = $edit_name;
                    break;
                case 2:
                    $edit_price = floatval(readline('Enter new price: '));
                    $product['price'] = $edit_price;
                    break;
                case 3:
                    $edit_count = intval(readline('Enter new count: '));
                    $product['count'] = $edit_count;
                    break;
                default:
                    echo 'Invalid value\n';
                    return;
            }
            echo "Product edited successfully.\n";
            return;
        }
    }
    
    echo "Product not found.\n";
}

function remove() {
    global $PRODUCTS;

    $product_delete = readline("Product ID => ");
    
    foreach ($PRODUCTS as $key => $product) {
        if ($product["code"] == $product_delete) {
            unset($PRODUCTS[$key]);
            echo "Product with ID {$product_delete} has been removed.\n";
            return;
        }
    }
    
    echo "Product with this ID {$product_delete} not found.\n"; 
}

function search() {
    global $PRODUCTS;

    $user_input = readline("Type your keyword => ");
    
    foreach ($PRODUCTS as $product) {
        if ($product['code'] == $user_input || stripos($product['name'], $user_input) !== false) { 
            echo "{$product['code']}\t{$product['name']}\t{$product['price']}\t{$product['count']}\n";
            return;
        }
    }
    
    echo 'Not found\n';
}

function show_list() {
    global $PRODUCTS;

    echo "Code\tName\tPrice\tCount\n";
    
    foreach ($PRODUCTS as $product) {
        echo "{$product['code']}\t{$product['name']}\t{$product['price']}\t{$product['count']}\n";
    }
}

function buy() {
    global $PRODUCTS;

    $user_input = readline("Enter the Product ID you want to buy: ");
    $quantity = intval(readline("Enter quantity: "));
    
    foreach ($PRODUCTS as &$product) {
        if ($product['code'] == $user_input) {
            if ($quantity <= $product['count']) {
                $total_cost = number_format($quantity * $product['price'], 2);
                $product['count'] -= $quantity;
                echo "You bought {$quantity} of {$product['name']} for \${$total_cost}.\n";

                if ($product['count'] == 0) {
                    remove();
                }
                return;
            } else {
                echo "Insufficient stock. Available count is {$product['count']}.\n";
                return;
            }
        }
    }

    echo "Product not found.\n";
}

function make_QRcode() {
    global $PRODUCTS;

    require_once 'phpqrcode/qrlib.php';

    $user_choose = readline('Product ID => ');
    
    foreach ($PRODUCTS as $product) {
        if ($user_choose == $product['code']) {
            QRcode::png(json_encode($product), 'code.png');
            echo "QR code generated and saved as 'code.png'.\n";
            return;
        }
    }

    echo "Product not found.\n";
}

function set_to_database() {
    global $PRODUCTS;

    if (empty($PRODUCTS)) {
        echo "No products to save.\n";
        return;
    }

    file_put_contents('database.txt', '');
    
    foreach ($PRODUCTS as $product) {
        file_put_contents('database.txt', implode(',', array_values($product)) . "\n", FILE_APPEND);
    }

   echo "Data saved to database.\n";
}

read_from_database();
echo "Data Loaded\n";

while (true) {
   show_menu();
   
   try {
       $user_input = readline('What is your choice => ');
       $choice = intval($user_input);
       
       switch ($choice) {
           case 1: add(); break;
           case 2: edit(); break;
           case 3: remove(); break;
           case 4: search(); break;
           case 5: show_list(); break;
           case 6: buy(); break;
           case 7: make_QRcode(); break; 
           case 8: set_to_database(); break;
           case 9:
               echo "Exiting program.\n";
               exit(0);
           default:
               echo "Invalid number, please try again.\n";
               break; 
       }

   } catch (ValueError | Exceptione) { 
       echo "Please enter a valid number.\n"; 
   }
}
?>