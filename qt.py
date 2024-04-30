from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import pandas as pd

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.login_window = QtWidgets.QWidget(LoginWindow)
        self.login_window.setStyleSheet("background-color: rgb(165, 200, 255);")
        self.login_window.setObjectName("MainWindow")
        self.username = QtWidgets.QPlainTextEdit(self.login_window)
        self.username.setGeometry(QtCore.QRect(310, 140, 171, 31))
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username.setObjectName("username")
        self.password = QtWidgets.QTextEdit(self.login_window)
        self.password.setGeometry(QtCore.QRect(310, 230, 171, 31))
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
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
        username = self.username.toPlainText()
        pass1 = self.password.toPlainText()
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
        LoginWindow.resize(1200, 800)
        LoginWindow.move(360, 140)

        self.main_table()

    # getting the table dimension
    def get_tablesize(self):
        cursor.execute("SELECT * FROM tbl_maintenance")
        result = cursor.fetchall()
        return result


    #create an excel like table object
    def main_table(self):
        table = QtWidgets.QTableWidget(self.login_window)
        table.setGeometry(QtCore.QRect(100, 100, 1000, 550))
        table.setObjectName("table")
        row = len(self.get_tablesize())
        columns = len(self.get_tablesize()[0])
        print(row,columns)
        table.setColumnCount(columns)  # Example: Set number of columns
        table.setRowCount(row)  # Example: Set number of rows
        # Example: Populate table with data
        for i in range(5):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem(f"Row {i + 1}, Col {j + 1}")
                table.setItem(i, j, item)
        table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        table.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
