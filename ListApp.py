import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication ,QWidget ,QListWidget ,QLabel ,QPushButton ,QVBoxLayout ,QHBoxLayout ,QLineEdit
import sys
import sqlite3 as sql


class List(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.Gui()
        self.data_to_list()

    def Gui(self):
        self.add_btn = QPushButton('Add')
        self.edit_btn = QPushButton('Edit')
        self.sort_btn = QPushButton('Sort')
        self.delete_btn = QPushButton('Delete')
        
        self.edit_btn.setEnabled(False)
        self.sort_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        
        h_add_box = QHBoxLayout()
        h_add_box.addWidget(self.add_btn)
        h_add_box.addWidget(self.sort_btn)
        h_add_box.addWidget(self.edit_btn)
        h_add_box.addWidget(self.delete_btn)
        
        self.input = QLineEdit()
        
        self.Todo_lst = QListWidget()
        v_box = QVBoxLayout()
        v_box.addWidget(self.Todo_lst)
        v_box.addWidget(self.input)
        v_box.addLayout(h_add_box)
        self.setLayout(v_box)
        
        self.add_btn.clicked.connect(self.add_func)
        self.edit_btn.clicked.connect(self.edit_func)
        self.delete_btn.clicked.connect(self.delete_func)
        self.sort_btn.clicked.connect(self.sort_func)
        self.Todo_lst.clicked.connect(self.clicked_lst)

    def add_func(self):
        if self.input.text() != '':
            self.sort_btn.setDisabled(False)
            self.Todo_lst.addItem(self.input.text())
            self.data = self.input.text()
            self.input.setText('')
            con=sql.connect('mydb.db')
            cur=con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Todo (list TEXT)''')
            cur.execute('INSERT INTO Todo(list) VALUES("{}")'.format(self.data))
            con.commit()
            con.close()
            
    def data_to_list(self):
        data=[]
        con=sql.connect('mydb.db')
        cur=con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Todo'")
        result = cur.fetchone()
        if result != None:
            self.sort_btn.setEnabled(True)
            row=cur.execute('SELECT * FROM Todo')
            for i in row :
                data.append(i)
            for i in data:
                self.Todo_lst.insertItem(self.Todo_lst.count(),i[0])
                
    def clicked_lst(self):
        self.current_value=self.Todo_lst.currentItem().text()
        if self.current_value != '':
            self.edit_btn.setEnabled(True)
            self.delete_btn.setEnabled(True)
            self.add_btn.setEnabled(False)
            self.sort_btn.setEnabled(False)
            self.input.setText(self.current_value)

    def edit_func(self):
        lst_value = self.input.text()
        index = self.Todo_lst.indexFromItem(self.Todo_lst.currentItem()).row()
        self.Todo_lst.takeItem(index)
        self.Todo_lst.insertItem(index,lst_value)
        self.input.setText('')
        self.edit_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.add_btn.setEnabled(True)
        self.sort_btn.setEnabled(True)
        con=sql.connect('mydb.db')
        cur=con.cursor()
        cur.execute(' UPDATE Todo SET list = "{}" WHERE list = "{}" '.format(lst_value,self.current_value))
        con.commit()
        con.close()
        
    def delete_func(self):
        index = self.Todo_lst.indexFromItem(self.Todo_lst.currentItem()).row()
        self.Todo_lst.takeItem(index)
        self.input.setText('')
        self.edit_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.add_btn.setEnabled(True)
        self.sort_btn.setEnabled(True)
        con=sql.connect('mydb.db')
        cur=con.cursor()
        cur.execute("DELETE FROM Todo WHERE list='{}'" .format(self.current_value))
        con.commit()
        con.close()
    
    def sort_func(self):
        pass
        




app=QApplication(sys.argv)
window=List()
window.show()
sys.exit(app.exec())
    