#coding:utf-8

def print_students(students):
 print u"Имя студента".ljust(15), \
 u"Группа".ljust(8), \
 u"Возраст".ljust(8), \
 u"Оценки".ljust(20)
 for student in students:
     print student["name"].ljust(15), \
     student["group"].ljust(8), \
     str(student["age"]).ljust(8), \
     str(student["marks"]).ljust(20)
     print "\n"


def find_students(students, avgmark):
    result = []

    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= 4:
            result.append(student)

    return result



groupmates = [
 {
 "name": u"Василий",
 "group": "912-2",
 "age": 19,
 "marks": [4, 3, 5, 5, 4]
 },
 {
 "name": u"Анна",
 "group": "912-1",
 "age": 18,
 "marks": [3, 2, 3, 4, 3]
 },
 {
 "name": u"Георгий",
 "group": "912-2",
 "age": 19,
 "marks": [3, 5, 4, 3, 5]
 },
 {
 "name": u"Валентина",
 "group": "912-1",
 "age": 18,
 "marks": [5, 5, 5, 4, 5]
 }
]
print u"\nСтуденты со средним баллом больше 4:"
good_students = find_students(groupmates, 4)
print_students(good_students)
