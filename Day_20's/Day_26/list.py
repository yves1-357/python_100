import random
names = ["Cassandra", "seani", "dave"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_student = {element: student_scores[element]  for element in student_scores if student_scores[element] > 60} 
print(passed_student)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

methode = [" FAIS_CECI pour CHAQUE_ELEMENT dans LISTE si CONDITION "]

# [ FAIS_CECI : C'est le résultat que tu veux (ex: n * 2, ou nom.upper()).
# pour CHAQUE_ELEMENT : C'est ta variable temporaire (ex: for n, for item).
# dans LISTE : C'est ta source de données (ex: in numbers, in names).
# si CONDITION ] : C'est ton filtre optionnel (ex: if n > 5).

# Liste
# nombres = [1, 2, 3, 4, 5]
# resulat = [carre * 2  for carre in nombres]
# print(resulat)

# Liste
noms = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
noms_courts = [element for element in noms if len(element) < 5]
print(noms_courts)

# Dictionnaire
scores = {"Alex": 88, "Beth": 92, "Caroline": 75, "Dave": 95}
resultats = {nom : "Reussi" if score > 80 else "echoué"  for (nom, score) in scores.items()}
print(resultats)