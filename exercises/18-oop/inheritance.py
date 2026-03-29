class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def walk(self):
        print("Walking")


class Student(Person):
    def __init__(self, student_id, fname, lname):
        super().__init__(fname, lname)
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id


teriz = Student(1, "Teriz", "De Ocampo")
teriz.walk()
print(teriz.student_id)
print(isinstance(teriz, Person))
