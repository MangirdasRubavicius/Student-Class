total_scores = 0
class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str):
            self.first_name = first_name
            self.last_name = last_name
            self.student_id = student_id
            self.exam_scores = []

    def add_score(self, score:int):
        if score >= 0 and score <= 100:
            exam_scores.append(score)
        else:
            return None


    def show_scores():
        for score in self.exam_scores:
                print(score, end=" ")
                print()

    def score_average(self):
        print(sum(self.exam_scores)+len(self.exam_scores))

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

p1 = Student(1, "John", "Doe")
p2 = Student(2, "Linda", "Jones")
p3 = Student(3, "Jason", "Kirk")
p4 = Student(4, "Jane", "Doe")

p1.add_score(100)
p1.add_score(95)

p2.add_score(25)
p2.add_score(65)
p2.add_score(80)
p2.add_score(75)

p3.add_score(50)
p3.add_score(60)
p3.add_score(55)

p4.add_score(95)
p4.add_score(80)
p4.add_score(100)

print("Average score:", s1.score_average())
print("Course passed?", s1.course_passed())


print("Average score:", s2.score_average())
print("Course passed?", s2.course_passed())


print("Average score:", s3.score_average())
print("Course passed?", s3.course_passed())


print("Average score:", s4.score_average())
print("Course passed?", s4.course_passed())
