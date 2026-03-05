from art import vs
from art import logo
import random
data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Plateforme de réseau social', 'country': 'États-Unis'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'Footballeur', 'country': 'Portugal'},
    {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musicienne et actrice', 'country': 'États-Unis'},
    {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'Acteur et catcheur professionnel', 'country': 'États-Unis'},
    {'name': 'Selena Gomez', 'follower_count': 174, 'description': 'Musicienne et actrice', 'country': 'États-Unis'},
    {'name': 'Kylie Jenner', 'follower_count': 172, 'description': 'Personnalité de télé-réalité et femme d’affaires', 'country': 'États-Unis'},
    {'name': 'Kim Kardashian', 'follower_count': 167, 'description': 'Personnalité de télé-réalité et femme d’affaires', 'country': 'États-Unis'},
    {'name': 'Lionel Messi', 'follower_count': 149, 'description': 'Footballeur', 'country': 'Argentine'},
    {'name': 'Beyoncé', 'follower_count': 145, 'description': 'Musicienne', 'country': 'États-Unis'},
    {'name': 'Neymar', 'follower_count': 138, 'description': 'Footballeur', 'country': 'Brésil'},
    {'name': 'National Geographic', 'follower_count': 135, 'description': 'Magazine et chaîne TV', 'country': 'États-Unis'},
    {'name': 'Justin Bieber', 'follower_count': 133, 'description': 'Musicien', 'country': 'Canada'},
    {'name': 'Taylor Swift', 'follower_count': 131, 'description': 'Musicienne', 'country': 'États-Unis'},
    {'name': 'Kendall Jenner', 'follower_count': 127, 'description': 'Mannequin et personnalité de télé-réalité', 'country': 'États-Unis'},
    {'name': 'Jennifer Lopez', 'follower_count': 119, 'description': 'Musicienne et actrice', 'country': 'États-Unis'},
    {'name': 'Nicki Minaj', 'follower_count': 113, 'description': 'Musicienne', 'country': 'Trinité-et-Tobago'},
    {'name': 'Nike', 'follower_count': 109, 'description': 'Marque de sport', 'country': 'États-Unis'},
    {'name': 'Khloé Kardashian', 'follower_count': 108, 'description': 'Personnalité de télé-réalité et femme d’affaires', 'country': 'États-Unis'},
    {'name': 'Miley Cyrus', 'follower_count': 107, 'description': 'Musicienne et actrice', 'country': 'États-Unis'},
    {'name': 'Katy Perry', 'follower_count': 94, 'description': 'Musicienne', 'country': 'États-Unis'},
    {'name': 'Kourtney Kardashian', 'follower_count': 90, 'description': 'Personnalité de télé-réalité', 'country': 'États-Unis'},
    {'name': 'Kevin Hart', 'follower_count': 89, 'description': 'Comédien et acteur', 'country': 'États-Unis'},

]


def choice_game():
     choix = random.choice(data)
     choix_2 = random.choice(data)
     game_should_continue = True
     current_score = 0
     print(logo)
     while game_should_continue:
          while choix == choix_2:
              choix_2 = random.choice(data)

          
          print(f"Compare A: {choix['name']}, a {choix['description']}, from {choix['country']}.")
          print(vs)
          print(f"Against B: {choix_2['name']}, a {choix_2['description']}, from {choix_2['country']}.")
          followers = str(input("Who has more followers : Type 'A'or 'B': ")).lower()
          


          if followers == "a" and choix['follower_count'] > choix_2['follower_count']:
            current_score += 1
            print(f"You're right! Current score : {current_score}. ")
            choix_2 = random.choice(data)
            
          elif followers == "b" and choix_2['follower_count'] > choix['follower_count']:
               current_score += 1
               print(f"You're right! Current score : {current_score}. ")
               choix = choix_2
               choix_2 = random.choice(data)

          else:
               print(f"Sorry, that's wrong. Final score: {current_score}")
               game_should_continue = False
               

choice_game()
while input("Do you want to re-do the game Type y/n: ").lower() == "y":
    print("\n" * 20)
    choice_game()
