from .student import Student

# add MiddleSchoolStudent here
# We would like to derive a MiddleSchoolStudent child class. 
# MiddleSchoolStudent will have all the attributes and behaviors of Student, but it will also:

# Track whether the student receives school transportation using the boolean attribute gets_transportation (can be set in the constructor, defaults to False)
# Update the summary method to include information about the student's transportation status
# Include tests for the additional functionality
# There is one test provided (currently commented out)
# Uncomment the test and implement the MiddleSchoolStudent class so that it passes
# If there is time, implement additional tests for the MiddleSchoolStudent class (review the HighSchoolStudent class for ideas

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes,
                gets_transportation = False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def display_transportation_message(self):
        get_message = "get" if self.gets_transportation else "does not get"
        return f"{self.name} {get_message} transportation"
    
    def summary(self):
        student_summary = super().summary()
        gets_transportion_message = self.display_transportation_message()
        
        return "\n".join(student_summary, gets_transportion_message)