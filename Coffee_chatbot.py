# This is a Codecademy assignment for a small system-initiative chatbot.
from utils import print_message, get_size, order_latte, order_mocha, choose_cup, yes_list, no_list

def coffee_bot():
  print('Welcome to the cafe!')

# Order the first drink
  order_drink = 'y'
# List to store drinks
  drinks = []

# Ordering the drink - collecting the order
  while order_drink in yes_list:
     size = get_size()  
     drink_type = get_drink_type()
     cup = choose_cup()


     drink = '{} {} in a {}'.format(size, drink_type, cup)
     print('Alright, that\'s a {}!'.format(drink))
     drinks.append(drink)

    # Keep asking if the customer wanted another drink if they enter anything besides yes or no
     while True:
      order_drink = input('Would you like to order another drink? (y/n) \n ')
      if (order_drink in yes_list) or (order_drink in no_list):
        break
  
# Print all drinks the customer has ordered, iterating through the list of drinks:
  print('So, I have: ')
  for drink in drinks:
    print('- ' + drink)

  # Ask for the customer's name
  name = input('Can I get your name please? \n> ')

  print('Thanks, {}! Your order will be ready shortly.'.format(name))

# Ask for the drink order
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Call the bot
coffee_bot()
