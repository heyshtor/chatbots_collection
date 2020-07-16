# This is a Codecademy assignment for a small system-initiative chatbot.

# Main bot
def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  cup = choose_cup()
  print("Alright, that's a {} {} in a {}!".format(size, drink_type, cup))

  name = input("Can I get your name please? \n")
  print("Thanks, {}! Your drink will be ready shortly.".format(name))


# Ask for the size of the drink
def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n ")

  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size() # now it becomes recursive function

# Generic error message for when no option is provided
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Ask for the drink order
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n ")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type() 

# Function for latte
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n ")
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte() 

# Ask about a cup
def choose_cup():
  res = input("Would you like a takeaway plastic cup or do you have a reusable cup? \n[a] Plastic cup \n[b] Reusable cup \n ")
  if res == 'a':
    return 'plastic cup'
  elif res == 'b':
    return 'reusable cup'
  else:
    print_message()
    return choose_cup()

# Calling the bot
coffee_bot()
