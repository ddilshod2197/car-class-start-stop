class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_gpa(self):
        total_points = 0
        for grade in self.grades:
            if grade >= 90:
                total_points += 4
            elif grade >= 80:
                total_points += 3
            elif grade >= 70:
                total_points += 2
            elif grade >= 60:
                total_points += 1
            else:
                total_points += 0
        return total_points / len(self.grades)


# Misol:
student = Student("Ali", [85, 90, 78, 92, 88])
print(student.calculate_gpa())
```

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_gpa(self):
        return sum(grade / 10 for grade in self.grades) / len(self.grades)


# Misol:
student = Student("Ali", [85, 90, 78, 92, 88])
print(student.calculate_gpa())
