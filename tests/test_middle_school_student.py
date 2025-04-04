from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation == False



def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 1 classes: Painting\nEllis get transportation"

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 1 classes: Painting\nEllis does not get transportation"

