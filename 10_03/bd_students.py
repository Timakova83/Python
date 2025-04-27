import json

def load_json():
    with open("domashka/10_03/students.json", "r", encoding="utf-8") as file:
        return json.load(file)

def new_student(id, name, age, group, gardes):
    data = load_json()
    for elem in data['students']:
            if id == elem['id']:
                return print(f'Такой студент уже есть!')
            
    data['students'].append({'id': id, 'name': name, 'age': age, 'group': group, 'gardes': gardes})
    with open("domashka/10_03/students.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print (data)
    

def delit_student(id):
    data = load_json()
    for elem in data['students']:
        if id == elem['id']:
            data['students'].remove(elem)

    with open("domashka/10_03/students.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
def average_ball():
    data = load_json()
    for elem in data['students']:
        average = sum(elem['gardes'])/len(elem['gardes'])
        print(f'Средний бал {elem['name']}: {average:.2f}')

def change_data(name: str, age=None, group=None, gardes=None):
    data = load_json()
    # Находим студента по ID
    student_found = False
    for student in data['students']:
        if student['name'] == name:
            student_found = True
            # Обновляем возраст
            if age is not None:
                student['age'] = age
            # Обновляем группу
            if group is not None:
                student['group'] = group
            # Добавляем новую оценку
            if gardes is not None:
                if 'grades' not in student:
                    student['grades'] = []  # Инициализируем список, если его нет
                student['grades'].append(gardes)
            break
            #     student['gardes'].append(gardes)
            # break

    if not student_found:
        print(f"Студент {name} не найден.")
        return

    # Записываем обновленные данные обратно в файл
    with open("domashka/10_03/students.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Данные студента {name} обновлены.")        

#new_student(1, "Иван Петров", 19, "A1", [5,4,3])
#new_student(2, "Анна Смирнова", 20, "B2", [4, 5, 5])
#new_student(3, "Ира Ковалева", 21, "B1", [4, 4, 5])
#delit_student(1)
average_ball()
change_data("Анна Смирнова", None, None, 5)