####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "pyCake"
signature_flavors = ["pure poison", "mud", "py", "toxic", "lethal"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ()
    print ("WELCOME TO PYCAKE! HERE\'S OUR MENU: ")
    print ()
    print ("Main items: ")
    for key in menu:
        print ( "* " + key + " | price: " + str(menu[key]) + " KD")


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print ()
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for i in original_flavors:
        print ("* " + i)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print ()
    print("Our signature flavor cupcakes (KD %s each):" % signature_price)
    # your code goes here!
    for i in signature_flavors:
        print ("* " + i)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    ch = False

    if order == "coffee" or order == "tea" or order == "bottled water" :
        ch = True

    else:        

        for i in original_flavors:
            if i == order:
                ch = True
                break
        
        for i in signature_flavors:
            if i == order:
                ch = True
                break

    return ch            


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order = input("Please enter your order: " + "(Enter the exact spelling of the item you want or type exit to checkout!) ")

    while order != "exit":
        if is_valid_order(order):
            order_list.append(order)

        else:
            print ("Invalid order! ")

        order = input()


    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True

    return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for i in order_list:
        if i == "tea":
            total += menu["tea"]
        elif i == "coffee":
            total += menu["coffee"]
        elif i == "bottled water":
            total += menu["bottled water"]
        else:
            for o in original_flavors:
                if i == o:
                    total += original_price

            for s in signature_flavors:
                if i == s:
                    total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    price = get_total_price(order_list)
    print("Your order is: ")
    for i in order_list:
        print ("- " + i)

    print ("That will be: " + str(price) + " KD")
    if accept_credit_card(price):
        print ("This order is eligible for credit card payment. ")
    else:
        print ("This order is NOT eligible for credit card payment. ")

    print ("Thank you for shopping at " + cupcake_shop_name + "! Please come again.")

