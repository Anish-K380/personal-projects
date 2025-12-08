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
        self.attendance = dict()

    def setClassTeacher(self):
        self.classTeacher = input('Enter class teacher:')

    def addStudent(self, rollNo):
        self.studentList.add(rollNo)

    def removeStudent(self, rollNo):
        self.studentList.remove(rollNo)

    def viewStudents(self, sManager):
        for roll in self.studentList:
            sManager.getStudent(roll)

    def createAttendance(self, date):
        self.attendance[date] = dict.fromkeys(self.studentList, True)

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

    def removeStudent(self, rollNo, bManager):
        if rollNo not in self.studentList:
            print('Roll number doesn\'t exist.')
        student = self.studentList[rollNo]
        self.names.remove(rollNo)
        branch = bManager.accessBranch[student.branch]
        branch.accessClass[student.section].removeStudent(rollNo)
        branch.removeStudent(rollNo)

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

    def markAttendance(self, date, classroom, sManager):
        if date in classroom.attendance:
            print('Record already exists.')
            return
        classroom.createAttendance(date)
        print('Enter a or A to mark absent. Leaving empty or other keys will be marked as present.')
        for i in classroom.studentList:
            student = sManager.studentList[i]
            if input(f'{student.name} : {student.rollNo} :').lower() == 'a':
                classroom.attendance[date][student.rollNo] = False

    def viewAttendance(self, date, classroom, sManager):
        conversion = {True : 'Present', False : 'Absent'}
        if date not in classroom.attendance:
            print('Record doesn\'t exist.')
            return
        print(date)
        for i in classroom.attendance[date]:
            student = sManager.studentList[i]
            print(f'{student.name} : {student.rollNo} : {conversion[classroom.attendance[date][i]]}')

class Institution:

    sManager = StudentManager()
    bManager = BranchManager()
    attendance = Attendance()
    while True:
        print('1. Mark attendance')
        print('2. View attendance')
        print('3. Add student')
        print('4. Alter student')
        print('5. Remove student')

        choice = int(input('Enter choice:'))
        if choice == 1:
            date = input('Enter date in format (dd.mm.yyyy):')
            branch = input('Enter branch:')
            if branch not in bManager.branchList:
                print('Branch doesn\'t exist.')
                continue
            branch = bManager.branchList[branch]
            section = input('Enter section:')
            if section not in branch.sections:
                print('Section doesn\'t exist.')
                continue
            section = branch.sections[section]
            attendance.markAttendance(date, section, sManager)
        
        elif choice == 2:
            date = input('Enter date in format (dd.mm.yyyy):')
            branch = input('Enter branch:')
            if branch not in bManager.branchList:
                print('Branch doesn\'t exist.')
                continue
            branch = bManager.branchList[branch]
            section = input('Enter section:')
            if section not in branch.sections:
                print('Section doesn\'t exist.')
                continue
            section = branch.sections[section]
            attendance.viewAttendance(date, section, sManager)

        elif choice == 3:
            sManager.create(bManager)

        elif choice == 4:
            rollNo = int(input('Enter roll number of student:'))
            if rollNo not in sManager.studentList:
                print('Roll number doesn\'t exist.')
                continue
            print('1. Alter name')
            print('2. Alter section')
            print('3. Alter branch')
            subChoice = int(input('Enter choice:'))

            if subChoice == 1:
                sManager.alterName(rollNo)

            elif subChoice == 2:
                sManager.alterSection(rollNo, bManager)
            
            elif subChoice == 3:
                sManager.alterBranch(rollNo, bManager)

            else:
                print('Incorrect choice selected.')

        elif choice == 5:
            rollNo = int(input('Enter roll number of student:'))
            if rollNo not in sManager.studentList:
                print('Roll number doesn\'t exist.')
                continue
            sManager.removeStudent(rollNo, bManager)
