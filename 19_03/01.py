
class Student:
    def __init__(self, name, age, grades = None):
        if grades is None:
            grades = []
        self.name = name
        self.age = age
        self.grades = grades
    
       
    
    def add_grade(self, grade): #todo 1. add_grade(grade): добавляет новую оценку.
        self.grades.append(grade)
    
    def get_average_grade(self): #todo 2. get_average_grade(): возвращает средний балл студента.
        if not self.grades:
            return 0  # Если оценок нет, возвращаем 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self): 
        #todo 3. display_info(): выводит информацию о студенте (имя, возраст, средний балл). 
        average_grade = self.get_average_grade()
        print(f'Студент: {self.name}')
        print(f'Возраст: {self.age} лет')  
        print(f'Средний балл: {average_grade:.2f}')

student = Student ("Vasya", 16, [4, 3, 5])
student.add_grade(4)
student.add_grade(5)
student.add_grade(5)
student.display_info()



