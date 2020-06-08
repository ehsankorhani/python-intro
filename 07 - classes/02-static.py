class Employee:
    firstname = ''
    lastname = ''
    monthly_bonus = 0.0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def add_task(self, title):
        pass

    @classmethod
    def set_bonus(cls, amount):
        cls.monthly_bonus = amount

it_manager = Employee('John', 'Doe')

Employee.set_bonus(1000)

print (Employee.monthly_bonus)
print (it_manager.monthly_bonus)


