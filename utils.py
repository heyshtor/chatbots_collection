
# Utils file for the coffee_chatbot

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

# Function for mocha
def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n ')
    if res == 'a':
      return 'pepperming mocha'
    elif res == 'b':
      return 'mocha'
    
    print_message()

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

# Generic error message for when no option is provided
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

yes_list = ['y', 'yes', 'yeah', 'ok', 'sure']
no_list = ['n', 'no', 'not', 'stop', 'bye']
