# # dictionnaries 
# colors_1 = {"Jaune": "Sara", "Yello": "Deani"}
# # print(colors_1["Yello"])
# colors_1["Loop"] = "Toi"
# print(colors_1)

# for i in colors_1:
#     print(i)
#     print(colors_1[i])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = ''
for i in student_scores:
    if student_scores[i] > 91 and student_scores[i] <= 100:
        student_grades = "Outstanding"
        print(f"{i} : {student_scores[i] } = {student_grades}")
    elif student_scores[i] > 81 and student_scores[i] <= 90:
        student_grades = "Exceeds Expectations"
        print(f"{i} : {student_scores[i] } = {student_grades}")
    elif student_scores[i] > 71 and student_scores[i] <= 80:
        student_grades = "Acceptable"
        print(f"{i} : {student_scores[i] } = {student_grades}")
    else:
        student_grades = "Fail"
        print(f"{i} : {student_scores[i] } = {student_grades}")