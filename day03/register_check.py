class RegisterCheck:
    def __init__(self):
        pass

    def register_check(self, input: dict) -> int:
        """
        Takes a dictionary with the student's attendance as a parameter and counts how many are currently in school.

        For example register = {'Michael':'yes','John': 'no','Peter':'yes', 'Mary': 'yes'} shoud return 3.

        :rtype: int
        :param input: Input dictionary with the student's attendance
        :return:  Count of students currently in school
        """
        students_in_school = 0
        for attendance in input.values():
            if attendance == 'yes':
                students_in_school += 1
        return students_in_school
