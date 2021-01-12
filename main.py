import random

print("Hi! What's your name?")
name = input()
print("Hi" + " " + name)
print("If you would like to leave, just press q")
print("What would you like to talk about today? Food, activities, books or music?")
chat = input()

quit_action = 'q'
if chat == 'q':
  print("Bye! Thanks for coming!")
  exit()

if chat == 'Food':
  favoriteFood = input("What's your favorite food?")
  print("That sounds delicious!")
  print("Which resturant serves the best" + favoriteFood + "?")
  resturantName = input()
  print("That's cool! I should try the" + favoriteFood + " " +"at" + " " + resturantName + "." + " " + "Sounds delicious!")

elif chat == 'activities':
  favoriteActivities = input("What's your favorite activity?")
  print("That's cool!" + favoriteActivities + " " + " sounds fun!")

elif chat == 'books':
  favoriteBooks = input("What's your favoite book?")
  print(favoriteBooks + " " + "is a great choice!")
  print("What other books do you like?")
  name = input()
  print("Excellent choice!")
  
elif chat == 'music':
  favoriteSong = input("What's your favorite song?")
  print(favoriteSong + " is a pretty good song. Good choice!")
  print("Whose your favorite music artist?")
  musicArtistName = input()
  print("Oh I have heard of " + musicArtistName + "!" + " I don't listen to" + " " + musicArtistName + ", but I should probably start listening! Seems like a good artist!")

elif chat == 'future':
  careerPath = input("What kind of job would you like to do when you're older?")
  careerName = input()
  print("Cool!")

else:
  def generate_response(user_input):
    responses = [
      "I'm sorry, I didn't understand. Can you try again?"
      "Looks like I have to go, sorry!"
    ]

    return random.choice(responses)
