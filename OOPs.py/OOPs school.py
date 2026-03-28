class Student:
    school = "ABC School"

    @classmethod
    def show_class(cls):
        print(cls)
        print(cls.school)

Student.show_class()