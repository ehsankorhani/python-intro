class Employee:
    firstname = ''
    lastname = ''

    def __init__(self, firstname, lastname):
        #pass
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        #return '{0} {1}'.format(Employee.firstname, Employee.lastname)
        return '{0} {1}'.format(self.firstname, self.lastname)

    def add_task(self, title):
        pass

it_manager = Employee('John', 'Doe')
developer = Employee('Jane', 'Doe')

#it_manager.firstname = 'John'

# print(Employee.__dict__)
# print(it_manager.__dict__)
# print(developer.__dict__)

print(it_manager.get_fullname())
print(developer.get_fullname())




#     def add_task(self, title):
#         self._tasks.append(title)

#     def report_tasks(self):
#         for task in self._tasks:
#             print(task)

# john = Employee()
# john.add_task('Setup spreadsheet')
# john.add_task('Enter information')

# john.report_tasks()

#return self.firstname + ' ' + self.lastname