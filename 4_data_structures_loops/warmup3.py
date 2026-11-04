group_1 = ["Python", "R", "JavaScript", "Java", "Ruby"]
group_2 = ["Python", "C++", "Ruby", "HTML"]

set_1 = set(group_1)
set_2 = set(group_2)

union = set_1.union(set_2)
print(f"Union: {union}")

intersection = set_1.intersection(set_2)
print(f"Intersection: {intersection}")

difference = set_1.difference(set_2)
print(f"Difference: {difference}")