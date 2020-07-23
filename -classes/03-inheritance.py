class Employee:
    firstname = ''
    lastname = ''
    tasks = []
    default_title = 'no name'

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def add_task(self, title = None):
        if (title == None):
            self.tasks.append(self.default_title)
        else:
            self.tasks.append(title)
    
    def get_tasks(self):
        return self.tasks


class Manager(Employee):
    _meetings = []
    default_title = 'metting'
    
    def __init__(self, firstname, lastname, office):
        super().__init__(firstname, lastname)
        #Employee.__init__(self, firstname, lastname)
        self.office = office

    def add_meeting(self, title):
        self._meetings.append(title)

    def report_meetings(self):
        for meeting in self._meetings:
            print(meeting)

mng_1 = Manager('John', 'Doe', 'M16')
#print (mng_1.__dict__)
print (mng_1.get_fullname())

#help(mng_1)

mng_1.add_task()
print(mng_1.get_tasks())
