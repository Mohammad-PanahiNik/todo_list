import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication ,QWidget ,QListWidget ,QLabel ,QPushButton ,QVBoxLayout ,QHBoxLayout ,QLineEdit
import sys

class List(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        
        self.add_btn = QPushButton('Add')
        self.delete_btn = QPushButton('Delete')
        self.edit_btn = QPushButton('Edit')
        self.sort_btn = QPushButton('Sort')
        
        self.delete_btn.setDisabled(True)
        self.edit_btn.setDisabled(True)
        self.sort_btn.setDisabled(True)
        
        h_add_box = QHBoxLayout()
        h_add_box.addWidget(self.add_btn)
        h_add_box.addWidget(self.edit_btn)
        h_add_box.addWidget(self.sort_btn)
        h_add_box.addWidget(self.delete_btn)
        
        self.input = QLineEdit()
        self.delete_btn = QPushButton('حذف')
        self.edit_btn = QPushButton('ویرایش')
        
        self.lst = QListWidget()
        v_box = QVBoxLayout()
        v_box.addWidget(self.lst)
        v_box.addWidget(self.input)
        v_box.addLayout(h_add_box)
        self.setLayout(v_box)
        




app=QApplication(sys.argv)
window=List()
window.show()
sys.exit(app.exec())
    