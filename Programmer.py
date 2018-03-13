# Programmer
class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)

    def school(self):
        print("His degree was a %s." % self.education)

class Employee(Person):
    def __init__(self, job):
        super(Employee, self).__init__(job)
        self.job = job

    def salary(self):
        print("The job, %s, is $20 per hour." % self.job)


class Programmer(Employee):
    def __init__(self, code):
        super(Programmer, self).__init__(code)
        self.code = code

    def job_work(self):
        print("The work is %s." % self.code)