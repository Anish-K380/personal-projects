import PyQt6.QtWidgets as qtw
from functools import partial
import csv

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = qtw.QWidget()
        
        self.layout = qtw.QStackedLayout()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

        initialize(self)

def initialize(window):
    selection_page = qtw.QHBoxLayout()
    selection_widget = qtw.QWidget()
    selection_widget.setLayout(selection_page)
    selection_page.addStretch(1)
    selection_buttons = qtw.QVBoxLayout()
    selection_buttons.addStretch(5)
    student_button = qtw.QPushButton('Student login')    #selection page
    teacher_button = qtw.QPushButton('Teacher login')
    student_button.clicked.connect(lambda: student_login(window))
    teacher_button.clicked.connect(lambda: teacher_login(window))
    selection_buttons.addWidget(student_button)
    selection_buttons.addStretch(1)
    selection_buttons.addWidget(teacher_button)
    selection_buttons.addStretch(5)
    selection_page.addLayout(selection_buttons)
    selection_page.addStretch(1)
    window.layout.addWidget(selection_widget)
    window.layout.setCurrentIndex(0)

    login_page = qtw.QHBoxLayout()
    login_widget = qtw.QWidget()
    login_widget.setLayout(login_page)
    credentials_layout = qtw.QVBoxLayout()
    user_id_layout = qtw.QHBoxLayout()
    login_submit_layout = qtw.QHBoxLayout()
    password_layout = qtw.QHBoxLayout()
    return_home_layout = qtw.QVBoxLayout()
    return_home_button = qtw.QPushButton('<=')
    return_home_button.clicked.connect(lambda : homepage(window))
    return_home_layout.addWidget(return_home_button)
    return_home_layout.addStretch(1)
    user_id = qtw.QLineEdit()
    password = qtw.QLineEdit()
    showPassword = qtw.QCheckBox('Show Password')
    showPassword.toggled.connect(lambda checked: password.setEchoMode(qtw.QLineEdit.EchoMode.Normal if checked else qtw.QLineEdit.EchoMode.Password))
    window.login_error_text = qtw.QLabel('')
    password.setEchoMode(qtw.QLineEdit.EchoMode.Password)
    user_id.setMinimumWidth(250)
    password.setMinimumWidth(250)                              #login page
    user_id_layout.addStretch(1)
    user_id_layout.addWidget(qtw.QLabel('User ID: '))
    user_id_layout.addWidget(user_id)
    user_id_layout.addStretch(1)
    password_layout.addStretch(1)
    password_layout.addWidget(qtw.QLabel('Password:'))
    password_layout.addWidget(password)
    password_layout.addStretch(1)
    login_create_new_button = qtw.QPushButton('Create new user')
    login_submit_button = qtw.QPushButton('Submit')
    login_submit_button.clicked.connect(partial(login_submit, user_id, password, window))
    login_submit_layout.addStretch(4)
    login_submit_layout.addWidget(login_create_new_button)
    login_submit_layout.addStretch(1)
    login_submit_layout.addWidget(login_submit_button)
    login_submit_layout.addStretch(4)
    credentials_layout.addStretch(3)
    credentials_layout.addLayout(user_id_layout)
    credentials_layout.addStretch(1)
    credentials_layout.addLayout(password_layout)
    credentials_layout.addWidget(showPassword)
    credentials_layout.addWidget(window.login_error_text)
    credentials_layout.addStretch(2)
    credentials_layout.addLayout(login_submit_layout)
    credentials_layout.addStretch(4)
    login_page.addLayout(return_home_layout)
    login_page.addStretch(1)
    login_page.addLayout(credentials_layout)
    login_page.addStretch(1)
    window.layout.addWidget(login_widget)

    user_widget = qtw,QWidget()
    user_layout = qtw.QVBoxLayout()
    user_widget.setLayout(user_layout)
    user_return_layout = qtw.QHBoxLayout()
    text_box1_layout = qtw.QHBoxLayout()
    text_box2_layout = qtw.QHBoxLayout()
    text_box3_layout = qtw.QHBoxLayout()
    window.teacherCodeWidget = qtw.QWidget()
    teacher_code_layout = qtw.QHBoxLayout()
    window.teacherCodeWidget.setLayout(teacher_code_layout)
    window.userError = qtw.QLabel('')
    user_submit_layout = qtw.QHBoxLayout()
    window.userReturn = qtw.QPushButton('<=')
    user_return_layout.addWidget(window.userReturn)
    user_return_layout.addStretch(1)
    window.text1 = qtw.QLabel('')
    window.text2 = qtw.QLabel('')
    window.text3 = qtw.QLabel('')
    textBox1 = qtw.QLineEdit()
    textBox2 = qtw.QLineEdit()
    textBox3 = qtw.QLineEdit()
    textBox1.setMinimumWidth(200)
    textBox2.setMinimumWidth(200)
    textBox3.setMinimumWidth(200)
    text_box1_layout.addStretch(1)
    text_box2_layout.addStretch(1)
    text_box3_layout.addStretch(1)
    text_box1_layout.addWidget(window.text1)
    text_box2_layout.addWidget(window.text2)
    text_box3_layout.addWidget(window.text3)
    text_box1_layout.addWidget(textBox1)
    text_box2_layout.addWidget(textBox2)
    text_box3_layout.addwidget(textBox3)
    text_box1_layout.addStretch(1)
    text_box2_layout.addStretch(1)
    text_box3_layout.addStretch(1)
    teacher_code_layout.addStretch(1)
    teacher_code_layout.addWidget(qtw.QLabel('Staff Code:'))
    teacherCode = qtw.QLineEdit()
    teacherCode.setMinimumWidth(200)
    teacher_code_layout.addWidget(teacherCode)
    teacher_code_layout.addStretch(1)
    user_submit_layout.addStretch(1)
    window.userSubmit = qtw.QPushButton('Submit')
    user_submit_layout.addWidget(window.userSubmit)
    user_submit_layout.addStretch(1)
    user_widget.addLayout(

homepage = lambda window : window.layout.setCurrentIndex(0)

def student_login(window):
    window.login_error_text.hide()
    window.currentMode = 0
    window.layout.setCurrentIndex(1)

def teacher_login(window):
    window.login_error_text.hide()
    window.currentMode = 1
    window.layout.setCurrentIndex(1)

def refresh():
    credentials.append({'Developer' : '8iJLVQAbHeVlQdyrDpiH'})
    credentials.append({'Developer' : '8iJLVQAbHeVlQdyrDpiH'})

def login_submit(user_id_obj, password_obj, window):
    user_id = user_id_obj.text()
    password = password_obj.text()
    if user_id in credentials[window.currentMode]:
        if password == credentials[window.currentMode][user_id]:
            window.userID = user_id
            window.password = password
        else:
            window.login_error_text.setText('Invalid Password')
            window.login_error_text.show()
    else:
        window.login_error_text.setText('Invalid user ID')
        window.login_error_text.show()

credentials = list()
topics = list()
refresh()
app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec()
