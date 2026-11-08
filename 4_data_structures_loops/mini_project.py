students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

#high scorers
high_scorers = []
for person in students:
    if person["score"] >75:
        high_scorers.append(person["name"])
print(f"High Scorers: {high_scorers}")

#highest scorer
highest_score = 75
top_student =""

for person in students:
    if person["score"] > highest_score:
        highest_score = person["score"]
        top_student = person["name"]

print(f"Top Student: {top_student}")


#class average
class_sum = 0
for person in students:
    class_sum += person["score"] 
class_average = class_sum/len(students)
print(f"Class average: {class_average}")

#unique subjects
unique_subjects = set()
for person in students:
    unique_subjects.add(person["subject"])
print(f"Unique subjects: {unique_subjects}")

