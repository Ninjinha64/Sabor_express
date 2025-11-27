import os # Importing os module for system commands

restaurants = [{'name':'Park', 'category':'Japanese','Active':False}, 
               {'name':'Burger House', 'category':'Fast Food','Active':True},
               {'name':'Pizza Place', 'category':'Italian','Active':False},
               {'name':'Corbute arrojado', 'category':'Brasileira','Active':False}] # List to store restaurant names



def show_the_name_of_program():

    """Shows the name of the program in ASCII art format."""



    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n      
""")

def show_options():

    """This function shows all the options available in the main menu."""


    print('1. Sign restaurant\n')
    print('2. List restaurant\n')
    print('3. Switching the state of the restaurant\n')
    print('4. Leave\n')

def shut_down_app(): # Shutting down the application
    """Shows the shutting down message."""


    show_sub_title('Shutting Down Application')

def return_to_main_menu():
    """Solicits user input to return to the main menu."""

    input('\nPress any key to back to the main menu ')
    main()

def unvalid_option(): # Handling unvalid options
    ''' This function handles unvalid options chosen by the user. 
    
    Outputs:
    - Prints an error message and returns to the main menu.
    '''
    print('Unvalid option!\n')
    return_to_main_menu()
    #input('Press any key to back to the main menu')
    #main()

def show_sub_title(text):
    ''' This function displays a subtitle with asterisks above and below it.
    
    Inputs:
    - text: The subtitle text to be displayed.
    '''


    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()


def Sign_Up_new_restaurant():
    '''This function is responsible for signing up a new restaurant.

       Inputs: 
       - Name of restaurant
       - Category of restaurant

       Outputs:
       - Added restaurant to the list of restaurants
    
    ''' 

    show_sub_title('Sign Up New Restaurant')
    name_of_restaurant = input('Enter the name of the restaurant: ')
    category = input(f'Type the name of the category from restaurant {name_of_restaurant}: ')
    data_from_restaurant = {'name':name_of_restaurant,'category':category,'Active':False}
    restaurants.append(data_from_restaurant)

    #restaurants.append(name_of_restaurant)
    print(f'The restaurant {name_of_restaurant} has been signed up successfully!\n') #pode ser isso

    return_to_main_menu()
    
    #TÁ COM ERRO POR AQUIIIIIIIIIIIIIIIII

def list_restaurants():
    show_sub_title('List of Restaurants') #os.system('cls')

    ''' This function lists all the restaurants with their details.
    
    Outputs:
    - Prints the name, category, and active state of each restaurant.
    '''

    print(f"{'Name of Restaurant'.ljust(22)} | {'Category'.ljust(20)} | State ")

    for restaurant in restaurants:
        name_restaurant = restaurant['name'] #getting the name of the restaurant
        category = restaurant['category'] #getting the category of the restaurant
        active = 'Actived' if restaurant['Active'] else 'Deactived' #checking if the restaurant is active or not

        print(f'- {name_restaurant.ljust(20)} | {category.ljust(20)} | {active}')
    
    return_to_main_menu()

def switch_restaurant_state():
    ''' This function switches the state of a restaurant between active and inactive.
    
    Outputs:
    - Prints a message indicating whether the restaurant has been activated or deactivated.
    '''



    show_sub_title('Switching Restaurant State')
    name_of_restaurant = input('Enter the name of the restaurant to switch its state: ')
    restaurante_found = False

    for restaurant in restaurants:
        if name_of_restaurant == restaurant ['name']: #(eu fiz uma alteração aqui)
            restaurante_found = True
            restaurant['Active'] = not restaurant['Active'] #(fiz uma alteração aqui)
            menssage = f'The restaurant {name_of_restaurant} has been actived successfully!' if restaurant['Active'] else f'The restaurante {name_of_restaurant} has been deactivated successfully!'
            print(menssage)
    if not restaurante_found: # If the restaurant is not found
        print('The restaurante was not found!') # print message




    return_to_main_menu()

def chose_option():
    ''' This function allows the user to choose an option from the main menu. 
    
    Outputs:
    - Calls the corresponding function based on the user's choice.
    '''


    try:
        option_chossed = int(input('Choose an option: '))
        # print(f'You chose option {option_chossed}')
        # option_chossed = int(option_chossed)




        if option_chossed == 1:
            Sign_Up_new_restaurant()

        elif option_chossed == 2:
            list_restaurants()

        elif option_chossed == 3:
            switch_restaurant_state()

        elif option_chossed == 4:
            shut_down_app()
        else:
            unvalid_option()
    except:
        unvalid_option()
    
def main():
    ''' Main function to run the application.'''
    os.system('cls')
    show_the_name_of_program()
    show_options()
    chose_option()

if __name__ == '__main__':
   main()
