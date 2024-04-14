class Student:
    def __init__(self, name, surname, gender, avg, average):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.avg = avg
        self.average = average
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}
        self.new_grades = {9,9}
    
    def students(self, list_student, list_course, gender, avg, average):
        self.gender = gender
        self.avg = avg
        self.average = average
        list_student = ['Ruoy', 'Eman']
        list_course = ['Python', 'Git']
        sum_grades = { }   
        
        for student in list_student:
            if (isinstance(student, Student) and list_course in student.grades):
                sum_grades.extend(student.grades[list_course])
        return round(sum(sum_grades) / len(sum_grades))
    
    def average_course(self, persons, course):
        self.persons= persons
        self.course = course
        list_student = ['Ruoy', 'Eman']
        new_grades = {9}
        all_average_grade = []
        for person in persons:
            if (isinstance(persons, Student) and list_student in person):
                all_average_grade.extend(person[list_student])
        if not all_average_grade:
            return round(sum(new_grades) / len(new_grades))
        return "There are no grades for this course"
        
    def __str__(self):
        avg = float(sum(self.new_grades) / len(self.new_grades))
        print(avg)
        return (f'{self.name}\n{self.surname}')
    
    def __lt__(self):
        return self.grades < self.avg   

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  

class Mentor:
    def __init__(self, name, surname, average_score):
        self.name = name
        self.surname = surname
        self.average_score = average_score
        self.courses_attached = []            
                
class Lecturer(Mentor):
    def __init__(self, name, surname, average):
        self.name = name
        self.surname = surname
        self.average = average
        self.grades = {9}
        
    def __str__(self):
        self.average = float(sum(self.grades) / len(self.grades))
        return str(self.average)
    
    def __lt__(self):
        return self.grades < self.average
    
    def average_course_lector(self, persons, course):
        self.persons= persons
        self.course = course
        list_lecture = ['Ruoy', 'Eman']
        new_grades = {9}
        all_average_grade = []
        for person in persons:
            if (isinstance(persons, Lecturer) and list_lecture in person):
                all_average_grade.extend(person[list_lecture])
        if not all_average_grade:
            return round(sum(new_grades) / len(new_grades))
        return "There are no grades for this course"
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return (f'{self.name}\n{self.surname}')
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender', 'average', 'avg')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy', 'average_score')
cool_mentor = Reviewer('Some', 'Buddy')
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy', 'average')
some_student = Student('Ruoy', 'Eman', 'gender', 'average', 'avg')

students = Student('Git', 'Python', 'average', 'gender', 'avg')
lectures = Lecturer('Git', 'Python', 'average')


students1 = Student( 'Helen', 'Bob', 'gender', 'avg', 'average')
students2 = Student('Helen', 'Bob', 'average', 'gender', 'avg')
students1.average_course('persons', 'course')

lectures1 = Lecturer('name', 'surname','average')
lectures1.average_course_lector('persons', 'course')
lectures2 = Lecturer('name', 'surname','average')

cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(lectures)
print(students)
print(some_reviewer)
print(some_lecturer)
print(some_student)
print('self.gardes' < 'self.average')
print('self.grades' < 'self.avg' )
print(f'Courses in progress: {"".join("Python, Git")}')
print(f'Completed courses: {"".join("Introduction to Programming")}')
print(f'The average grade of all students in the Python course: {students1.average_course("persons", "course")}')
print(f'The average grade of all lecturers in the Python course: {lectures1.average_course_lector('persons', 'course')}')