import random
states = ["virginia", "georgia", "jolie"]
states[1] = "toronto"
states.append("hola")
print(states)
print(states[20])

friends = ["Alice", "Sara", "Charlotte", "Georgia", "Yuri"]
random_card_friends = random.choice(friends)
print(random_card_friends)