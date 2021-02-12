# import random

quit_action = 'q'

def get_input(text):
  return input(text)

def chat_Food():
  # return "What's your favorite cuisine?"
  favoriteFood = input("What's your favorite food?")
  print("That sounds delicious!")
  print("Which resturant serves the best" + favoriteFood + "?")
  resturantName = input()
  print("That's cool! I should try the" + favoriteFood + " " +"at" + " " + resturantName + "." + " " + "Sounds delicious!")

def chat_Activities():
  print(activities_handler())

def activities_handler():
  favoriteActivity = get_input("What's your favorite activity?")
  if favoriteActivity == 'coding':
    return 'Coding is the coolest!'
  else:
    return "That's cool! " + favoriteActivity + " sounds fun!"


def chat_Books():
  favoriteBooks = input("What's your favoite book?")
  print(favoriteBooks + " " + "is a great choice!")
  print("What other books do you like?")
  name = input()
  print("Excellent choice!")

def chat_Music():    
  favoriteSong = input("What's your favorite song?")
  print(favoriteSong + " is a pretty good song. Good choice!")
  print("Whose your favorite music artist?")
  musicArtistName = input()
  print("Oh I have heard of " + musicArtistName + "!" + " I don't listen to" + " " + musicArtistName + ", but I should probably start listening! Seems like a good artist!")
  print("What other artists do you listen to?")
  print("You have good taste in music!")

def chat_Future():
  dreams = input("What do you want to do in the future?")
  print("Cool!")

  # else:
  #   def generate_response(user_input):
  #     responses = [
  #       "I'm sorry, I didn't understand. Can you try again?"
  #       "Looks like I have to go, sorry!"
  #       "I have to go! Talk to you later, bye!"
        
  #     ]

  #     return random.choice(responses)

# handle_input returns a bool indicating if the input
# from the user was able to be routed to a different method successfully
# True = success
# False = failed
def handle_input(user_input):
  if user_input == 'food':
    chat_Food()
  elif user_input == 'activities':
    chat_Activities()
  elif user_input == 'music':
    chat_Music()
  elif user_input == 'future':
    chat_Future()
  elif user_input == quit_action:
    # https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement
    pass
  else:
    # unhandled input from user!
    return False
  return True
  

def main():
  print("Hi! What's your name?")
  name = input()
  print("Hi" + " " + name)
  print("If you would like to leave, just press q")

  chat = ''
  while chat != quit_action:
    chat = input("What would you like to talk about today? Food, activities, books or music?")
    success = handle_input(chat)
    if success == False:
      print("I'm sorry, I didn't understand. Let's try again.")

  print("Bye! Thanks for coming!")
  exit()

if __name__ == '__main__':
  main()
