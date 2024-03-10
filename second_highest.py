students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90], ['Chien', 92]]

def second_highest(students):
	second_score = find_second_score_value(students)
	second_students = find_second_score_students(students, second_score)
	print(second_students)


def find_second_score_value(students):
	scores = []
	for student in students:
		scores.append(student[1])
	scores.sort(reverse = True)
	check = scores[0]
	second_score = scores[0]
	for score in scores:
		if score < check:
			second_score = score
			break
	return second_score


def find_second_score_students(students, second_score):
	second_students = []
	for student in students:
		if student[1] == second_score:
			second_students.append(student)
	return second_students

second_highest(students)