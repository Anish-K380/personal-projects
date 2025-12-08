from datetime import date
class Student:

    def __init__(self):
        self.name = input('Enter name:')
        self.rollNo = int(input('Enter roll number:'))
        self.branch = input('Enter Branch:')
        self.section = input('Enter Section')
    
    def alterName(self):
        self.name = input('Enter name:')

    def alterBranch(self):
        self.branch = input('Enter new branch:')
        self.alterSection()

    def alterSection(self):
        self.section = input('Enter new section:')

    def details(self):
        print('name:', self.name)
        print('Roll No:', self.rollNo)
        print('Branch:', self.branch)
        print('Section:', self.section)

class Branch:

    def __init__(self, branch):
        self.name = branch
        self.studentList = set()
        self.sections = dict()

    def addStudent(self, roll):
        self.studentList.add(roll)

    def removeStudent(self, roll):
        self.studentList.remove(roll)  

    def viewStudents(self, sManager):
        for roll in self.studentList:
            sManager.getStudent(roll)

    def manageSection(self, section, rollNo):
        if section not in self.sections:
            self.addSection(section)
        self.sections[section].addStudent(rollNo)

    def addSection(self, section):
        self.sections[section] = Classroom(self.name, section)

    def accessClass(self, section):
        if section in self.sections:
            return self.sections[section]
        print('Classroom doesn\'t exist')

class Classroom:

    def __init__(self, branch, section):
        self.branch = branch
        self.section = section
        self.classTeacher = None
        self.studentList = set()

    def setClassTeacher(self):
        self.classTeacher = input('Enter class teacher:')

    def addStudent(self, rollNo):
        self.studentList.add(rollNo)

    def removeStudent(self, rollNo):
        self.studentList.remove(rollNo)

    def viewStudents(self, sManager):
        for roll in self.studentList:
            sManager.getStudent(roll)

class StudentManager:

    def __init__(self):
        self.studentList = dict()
        self.names = dict()

    def create(self, bManager):
        student = Student()
        if student.rollNo in self.studentList:
            print('Roll number already in use.')
            return
        self.studentList[student.rollNo] = student
        self.manageName(student.name, student.rollNo)
        bManager.manage(student.branch, student.section, student.rollNo)

    def manageName(self, name, rollNo):
        if name in self.names:
            self.names[name].add(rollNo)
        else:
            self.names[name] = {rollNo}

    def getStudent(self, rollNo):
        if rollNo in self.studentList:
            self.studentList[rollNo].details()
        else:
            print('Roll Number doesn\'t exist')

    def alterName(self, rollNo):
        if rollNo in self.studentList:
            student = self.studentList[rollNo]
            student.details()
            if input('Do you want to change the name? (Y/N)') == 'Y':
                self.names[student.name].remove(student.rollNo)
                student.alterName()
                self.manageName(student.name, student.rollNo)
        else:
            print('Roll number doesn\'t exist.')

    def alterSection(self, rollNo, bManager):
        if rollNo in self.studentList:
            student = self.studentList[rollNo]
            student.details()
            if input('Do you want to change the section? (Y/N)') == 'Y':
                branch = bManager.accessBranch(student.branch)
                branch.accessClass(student.section).removeStudent(rollNo)
                student.alterSection()
                branch.manageSection(student.section, student.rollNo)
        else:
            print('Roll number doesn\'t exist.')

    def alterBranch(self, rollNo, bManager):
        if rollNo in self.studentList:
            student = self.studentList[rollNo]
            student.details()
            if input('Do you want to change the branch? (Y/N)') == 'Y':
                prevBranch = bManager.accessBranch(student.branch)
                prevBranch.accessClass(student.section).removeStudent(rollNo)
                prevBranch.removeStudent(rollNo)
                student.alterBranch()
                student.alterSection()
                bManager.manage(student.branch, student.section, student.rollNo)


class BranchManager:

    def __init__(self):
        self.branchList = dict()

    def create(self, branch):
        self.branchList[branch] = Branch(branch)

    def manage(self, branch, section, rollNo):
        if branch not in self.branchList:
            self.create(branch)
        self.branchList[branch].addStudent(rollNo)
        self.branchList[branch].manageSection(section, rollNo)

    def accessBranch(self, branch):
        if branch in self.branchList:
            return self.branchList[branch]
        else:
            print('Branch doesn\'t exist.')

class Attendance:

    def __init__(self):
        self.
