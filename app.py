import os

products = [
    {'name': 'toddy', 'price': 1.00, 'amount': 2}, 
    {'name': 'rap10', 'price': 8.00, 'amount': 1}
    ]

def menu():
    os.system('cls')
    print('1 - CREATE')
    print('2 - READ')
    print('3 - UPDATE')
    print('4 - DELETE')
    print('5 - EXIT')

def invalid_option():
    print('invalid option\n')
    back_menu()

def exit_program():
    os.system('cls')
    print('Bye')

def back_menu():
    print()
    input('<-- back to menu')
    main()

def show_subtitles(text):
    os.system('cls')
    print(text, '\n\n')

def create_product():
    show_subtitles('Create a new product:')

    name = input('Name:')
    price = float(input('Price:'))
    amount = int(input('Amount:'))

    product = {'name': name, 'price': price, 'amount': amount}

    products.append(product)

    print(f'{name} created')

    back_menu()

def read_products():
    show_subtitles('Show all products')

    print(f'product  |   price    |   amount')

    total = 0

    for product in products:
        name = product['name']
        price = product['price']
        amount = product['amount']

        # calcula total da compra
        total += amount*price

        print(f'{name}    |   {price}      |   {amount}')

    print(f'\n                      Total: {total}')

    back_menu()

def update_product():
    show_subtitles('Update product')
    
    product_name = input('What product do you want update?\n')

    print('1 - Name')
    print('2 - Price')
    print('3 - Amount')

    option = int(input('Pick the property to change\n'))

    if option in (1, 2, 3):

        new_property = input('Type new value\n')

        product_search = False

        for product in products:
            if product['name'] == product_name:
                product_search = True

                match option:
                    case 1:
                        product['name'] = new_property
                    case 2:
                        product['price'] = float(new_property)
                    case 3:
                        product['amount'] = int(new_property)
                    case _:
                        invalid_option()

                print('product updated')
        
        if product_search == False:
            print('Product not found\n')

        back_menu()
    else:
        invalid_option()

def delete_product():
    show_subtitles('Delete product')
    
    product_name = input('What product do you want delete?\n')

    product_search = False

    for product in products:
        if product['name'] == product_name:
            product_search = True
            products.remove(product)
            print('product deleted')
    
    if product_search == False:
            print('Product not found\n')

    back_menu()

def setOption():
    try:
        option = int(input())
        match option:
            case 1:
                print('case 1')
                create_product()
            case 2:
                print('case 2')
                read_products()
            case 3:
                print('case 3')
                update_product()
            case 4:
                print('case 4')
                delete_product()
            case 5:
                print('case 5')
                exit_program()
            case _:
                invalid_option()
    except:
        invalid_option()

def main():
    menu()
    setOption()
    
if __name__ == '__main__':
    main()