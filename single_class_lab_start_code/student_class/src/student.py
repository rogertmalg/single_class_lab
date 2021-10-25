class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def test_student_has_name(self):
        return student.name

    def test_student_has_cohort(self):
        return student.cohort

    def test_student_can_update_name(self):
        student.name = "Mike"
        
    def test_student_can_change_cohort(self):
        student.cohort = "G21"

