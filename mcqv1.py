import PyQt6.QtWidgets as qtw
import csv

class MainWindow(qtw.QMainWindow()):
    def __init__():
        super().__init__()
        self.central_widget = qtw.QWidget()
        
        self.layout = qtw.QStackedLayout()

        self.setCentralWidget(self.central_widget)

def initialize(window):
    selection_page = qtw.QHBoxLayout()
    selection_widget = qtw.QWidget()
    selection_widget.setLayout(selection_page)
    selection_page.addStretch(1)
    selelction_buttons = qtw.QVBoxLayout()
    selection_buttons.addStretch(3)
    student_button = qtw.QButton('Student login')    #login page
    teacher_button = qtw.QButton('Teacher login')
    selection_buttons.addWidget(student_button)
    selection_buttons.addStretch(1)
    selection_buttons.addWidget(teacher_button)
    selection_buttons.addStretch(3)
    selection_page.addLayout(selection_buttons)
    selection_page.addStretch(1)
    window.layout.addWidget(selection_widget)

    login_page = qtw.QHBoxLayout()
    login_widget = qtw.QWidget()
