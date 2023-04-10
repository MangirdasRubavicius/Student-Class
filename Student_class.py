total_scores = 0
class Student:
    def __init__(self, student_id, first_name, last_name, exam_scores):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.student_id = int(student_id)
        self.exam_scores = exam_scores[int()]

def add_score(score):
    if score >= 0 and score <= 100:
        exam_scores.append(score)
    else:
        return None


def show_scores():
    print(exam_scores)

def score_average():
    print(sum(exam_scores)+len(exam_scores))

def course_passed():
    for i in exam_scores.values():
        if exam_scores.values(i) > 60:
            total_scores = total_scores + 1
        else:
            return

    if total_scores >= 3:
        return True

    else:
        return False

p1 = Student(1, "John", "Doe", [100, 95])
p2 = Student(2, "Linda", "Jones", [25, 65,80,75])
p3 = Student(3, "Jason", "Kirk", [50, 60,55])
p4 = Student(4, "Jane", "Doe", [95, 80,100])

show_scores()

course_passed()

add_score(50)
