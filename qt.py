from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import pandas as pd
import datetime as dt

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.login_window = QtWidgets.QWidget(LoginWindow)
        self.login_window.setStyleSheet("background-color: rgb(165, 200, 255);")
        self.login_window.setObjectName("MainWindow")
        self.username = QtWidgets.QLineEdit(self.login_window)
        self.username.setGeometry(QtCore.QRect(310, 140, 171, 31))
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username.setObjectName("username")
        self.username.setText("postgres")
        self.password = QtWidgets.QLineEdit(self.login_window)
        self.password.setGeometry(QtCore.QRect(310, 230, 171, 31))
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setText("mbpi")
        self.login_btn = QtWidgets.QPushButton(self.login_window)
        self.login_btn.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.login_btn.setStyleSheet("\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.login_btn.setObjectName("Login")
        self.login_btn.clicked.connect(self.login)
        LoginWindow.setCentralWidget(self.login_window)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(LoginWindow)
        self.toolBar.setObjectName("toolBar")
        LoginWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MBPI"))
        self.login_btn.setText(_translate("LoginWindow", "Login"))
        self.toolBar.setWindowTitle(_translate("LoginWindow", "toolBar"))

    def login(self):
        username = self.username.text()
        pass1 = self.password.text()
        try:
            conn = psycopg2.connect(
                host='localhost',
                port=5432,
                dbname="MBPI",
                user=username,
                password=pass1)
            global cursor
            cursor = conn.cursor()
            print("Connected Successfully")
            self.launch_main()
        except Exception as e:
            print("Invalid Credentials:", e)



    #This is the main window after login screen
    def launch_main(self):
        # Delete widgets
        self.username.deleteLater()
        self.password.deleteLater()
        self.login_btn.deleteLater()

        # Setting the size and position of the main window
        LoginWindow.setFixedSize(1200, 900)  #fixed size
        LoginWindow.move(360, 140)

        #add the table to the Window
        self.main_table()
        self.table.itemSelectionChanged.connect(self.show_selected) #Selection updates
        #Itemname textbox
        self.itemname_box = QtWidgets.QLineEdit(self.login_window)
        self.itemname_box.setGeometry(QtCore.QRect(100, 620, 190, 30))
        self.itemname_box.setStyleSheet("background-color: white;")
        self.itemname_box.setFont(QtGui.QFont("Arial", 11))
        self.itemname_box.setAutoFillBackground(False)
        self.itemname_box.show()

        #Itemname Label
        self.itemname_label = QtWidgets.QLabel(self.login_window)
        self.itemname_label.setText("Item Name")
        self.itemname_label.setGeometry(QtCore.QRect(155, 650, 100, 30))
        self.itemname_label.setAutoFillBackground(False)
        self.itemname_label.setFont(QtGui.QFont("Arial", 11))
        self.itemname_label.show()

        #Quantity textbox
        self.quantity_box = QtWidgets.QLineEdit(self.login_window)
        self.quantity_box.setGeometry(QtCore.QRect(340, 620, 70, 30))
        self.quantity_box.setStyleSheet("background-color: white;")
        self.quantity_box.setFont(QtGui.QFont("Arial", 11))
        self.quantity_box.setAutoFillBackground(False)
        self.quantity_box.show()

        #Quantity Label
        self.quantity_label = QtWidgets.QLabel(self.login_window)
        self.quantity_label.setText("Quantity")
        self.quantity_label.setGeometry(QtCore.QRect(345, 650, 70, 30))
        self.quantity_label.setAutoFillBackground(False)
        self.quantity_label.setFont(QtGui.QFont("Arial", 11))
        self.quantity_label.show()

        #Unit textbox
        self.unit_box = QtWidgets.QLineEdit(self.login_window)
        self.unit_box.setGeometry(QtCore.QRect(460, 620, 70, 30))
        self.unit_box.setStyleSheet("background-color: white;")
        self.unit_box.setFont(QtGui.QFont("Arial", 11))
        self.unit_box.setAutoFillBackground(False)
        self.unit_box.show()

        #Unit Label
        self.unit_label = QtWidgets.QLabel(self.login_window)
        self.unit_label.setText("Unit")
        self.unit_label.setGeometry(QtCore.QRect(480, 650, 70, 30))
        self.unit_label.setAutoFillBackground(False)
        self.unit_label.setFont(QtGui.QFont("Arial", 11))
        self.unit_label.show()

        #model textbox
        self.model_box = QtWidgets.QLineEdit(self.login_window)
        self.model_box.setGeometry(QtCore.QRect(600, 620, 190, 30))
        self.model_box.setStyleSheet("background-color: white;")
        self.model_box.setFont(QtGui.QFont("Arial", 10))
        self.model_box.setAutoFillBackground(False)
        self.model_box.show()

        #model label
        self.model_label = QtWidgets.QLabel(self.login_window)
        self.model_label.setText("Model")
        self.model_label.setGeometry(QtCore.QRect(680, 650, 70, 30))
        self.model_label.setAutoFillBackground(False)
        self.model_label.setFont(QtGui.QFont("Arial", 11))
        self.model_label.show()

        #remarks textbox
        self.remarks_box = QtWidgets.QLineEdit(self.login_window)
        self.remarks_box.setGeometry(QtCore.QRect(850, 620, 190, 30))
        self.remarks_box.setStyleSheet("background-color: white;")
        self.remarks_box.setFont(QtGui.QFont("Arial", 10))
        self.remarks_box.setAutoFillBackground(False)
        self.remarks_box.show()

        #remarks label
        self.remarks_label = QtWidgets.QLabel(self.login_window)
        self.remarks_label.setText("Remarks")
        self.remarks_label.setGeometry(QtCore.QRect(920, 650, 70, 30))
        self.remarks_label.setAutoFillBackground(False)
        self.remarks_label.setFont(QtGui.QFont("Arial", 11))
        self.remarks_label.show()

        #This part below is for showing logs


        #Encoded By Label
        self.encoded_by = QtWidgets.QLabel(self.login_window)
        self.encoded_by.setText("Encoded By: ")
        self.encoded_by.setGeometry(QtCore.QRect(100, 700, 100, 25))
        self.encoded_by.setAutoFillBackground(False)
        self.encoded_by.setFont(QtGui.QFont("Arial", 12))
        self.encoded_by.setStyleSheet('color: red')
        self.encoded_by.show()

        #Encoded Date Label
        self.encoded_date = QtWidgets.QLabel(self.login_window)
        self.encoded_date.setText("Date Encoded: ")
        self.encoded_date.setGeometry(QtCore.QRect(100, 723, 100, 25))
        self.encoded_date.setAutoFillBackground(False)
        self.encoded_date.setFont(QtGui.QFont("Arial", 12))
        self.encoded_date.setStyleSheet('color: red')
        self.encoded_date.show()

        #Updated By Label
        self.updated_by = QtWidgets.QLabel(self.login_window)
        self.updated_by.setText("Updated By: ")
        self.updated_by.setGeometry(QtCore.QRect(100, 746, 100, 25))
        self.updated_by.setAutoFillBackground(False)
        self.updated_by.setFont(QtGui.QFont("Arial", 12))
        self.updated_by.setStyleSheet('color: red')
        self.updated_by.show()

        #Date Updated Label
        self.updated_date = QtWidgets.QLabel(self.login_window)
        self.updated_date.setText("Updated By: ")
        self.updated_date.setGeometry(QtCore.QRect(100, 769, 100, 25))
        self.updated_date.setAutoFillBackground(False)
        self.updated_date.setFont(QtGui.QFont("Arial", 12))
        self.updated_date.setStyleSheet('color: red')
        self.updated_date.show()





    # getting the table dimension
    def get_tablesize(self):
        cursor.execute("SELECT * FROM tbl_maintenance")
        result = cursor.fetchall()
        return result





    #create an excel like table object
    def main_table(self):

        self.table = QtWidgets.QTableWidget(self.login_window)

        # Set table size
        self.table.setGeometry(QtCore.QRect(100, 50, 1000, 550))
        self.table.setObjectName("table")
        self.table.setStyleSheet("background-color: white;")

        # Fetch table data and column names
        query_result = self.get_tablesize()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'tbl_maintenance';") #query for getting the table names
        column_names = [col[0] for col in cursor.fetchall()]

        self.rows = len(query_result)
        self.columns = len(query_result[0])

        self.table.setColumnCount(self.columns)  # Set number of columns
        self.table.setRowCount(self.rows)  # Set number of rows

        # Populate table with data
        for i in range(self.rows):
            for j in range(self.columns):
                item = QtWidgets.QTableWidgetItem(str(query_result[i][j]))  # Convert to string
                self.table.setItem(i, j, item)

        self.table.setHorizontalHeaderLabels(column_names)
        self.table.show()
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


    def show_selected(self):
        selected = self.table.selectedItems()
        if selected:
            items = [item.text() for item in selected]
            print(len(selected))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
