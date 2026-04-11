import random
names = ["Cassandra", "seani", "dave"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_student = {element: student_scores[element]  for element in student_scores if student_scores[element] > 60} 
print(passed_student)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
