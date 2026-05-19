fruits = ["Banane", "Pommes", "Mangue", "Kiwi"]
print(fruits)

# student_score = [180, 124, 165, 173, 289, 169, 146]

# # score = max(student_score)

# # max_score = 0
# # for score in student_score:
# #     # score = max(student_score)
# #     if score > max_score:
# #         max_score = score
# # print(max_score)
# number = [180, 124, 165, 173, 289, 169, 146]
# somme = 0
# for i in range(1, 101):
#     somme = somme + i
# print(somme)

for i in range(1, 10):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
      print(i)
