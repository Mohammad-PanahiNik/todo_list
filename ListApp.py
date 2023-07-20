import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication ,QWidget ,QListWidget ,QLabel ,QPushButton ,QVBoxLayout ,QHBoxLayout ,QLineEdit
import sys

class List(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        
        self.input = QLineEdit()
        self.add_btn = QPushButton('اضافه کردن')
        h_add_box = QHBoxLayout()
        h_add_box.addWidget(self.input)
        h_add_box.addWidget(self.add_btn)
        
        self.delete_btn = QPushButton('حذف')
        self.edit_btn = QPushButton('ویرایش')
        
        self.lst = QListWidget()
        v_box = QVBoxLayout()
        v_box.addWidget(self.lst)
        v_box.addLayout(h_add_box)
        self.setLayout(v_box)
        




app=QApplication(sys.argv)
window=List()
window.show()
sys.exit(app.exec())
    