class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def __repr__(self):
        return "Employee('{}', '{}')".format(self.firstname, self.lastname)

    def __str__(self):
        return "{} - {}".format(self.firstname, self.lastname)
        

emp_01 = Employee('Jane', 'Doe')

print(emp_01.__repr__())
print(emp_01.__str__())
