from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
import psycopg2
import pandas as pd
import datetime as dt



class ClickableLabel(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.login_window = QtWidgets.QWidget(LoginWindow)
        self.login_window.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(176, 0, 0, 255), stop:0.738636 rgba(255, 113, 250, 255))")
        self.login_window.setObjectName("MainWindow")
        self.username = QtWidgets.QLineEdit(self.login_window)
        self.username.setGeometry(QtCore.QRect(310, 140, 171, 31))
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px")
        self.username.setObjectName("username")
        self.username.setText("postgres")
        self.password = QtWidgets.QLineEdit(self.login_window)
        self.password.setGeometry(QtCore.QRect(310, 230, 171, 31))
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setText("mbpi")
        self.login_btn = QtWidgets.QPushButton(self.login_window)
        self.login_btn.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.login_btn.setStyleSheet("\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(255, 255, 255); \n"
                                     "border-radius: 10px;")
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
            self.conn = psycopg2.connect(
                host='192.168.1.13',
                port=5432,
                dbname="MBPI",
                user="postgres",
                password="mbpi")
            global cursor
            cursor = self.conn.cursor()
            print("Connected Successfully")
            self.launch_main()
        except Exception as e:
            print("Invalid Credentials:", e)

    # This is the main window after login screen
    def launch_main(self):
        # Delete widgets
        try:
            self.username.deleteLater()
            self.password.deleteLater()
            self.login_btn.deleteLater()
        except:
            pass
        self.login_window.setStyleSheet("background-color: white")
        # Setting the size and position of the main window
        LoginWindow.setFixedSize(1200, 900)  # fixed size
        LoginWindow.move(360, 100)

        # add the table to the Window
        self.show_table()
        self.table.itemSelectionChanged.connect(self.show_selected)  # Selection updates


        # This part below is for Information Box

        self.info_box = QtWidgets.QWidget(self.login_window)
        self.info_box.setGeometry(QtCore.QRect(80, 560, 1031, 270))
        self.info_box.setStyleSheet("""
        background-color: white;
        border-top-left-radius: 20px; 
        border-top-right-radius: 20px; 
        border-bottom-left-radius: 20px; 
        border-bottom-right-radius: 20px;
        border: 2px solid rgb(0,109,184)
        """)
        self.info_box.show()

        self.info_border = QtWidgets.QWidget(self.login_window)
        self.info_border.setGeometry(QtCore.QRect(80, 560, 1031, 60))
        self.info_border.setStyleSheet(
            "background-color: rgb(0,109,184); border-top-left-radius: 20px; border-top-right-radius: 20px;")
        self.info_border.show()



        # Date Label
        self.date_label = QtWidgets.QLabel(self.login_window)
        self.date_label.setGeometry(QtCore.QRect(1000, 10, 150, 20))
        self.date_label.setStyleSheet("background-color: white")
        self.date_label.show()

        self.timer = QtCore.QTimer(self.login_window)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)


        #Add Entry Button
        self.add_btn_icon = ClickableLabel(self.login_window)
        self.add_btn_icon.setGeometry(1125, 100, 50, 50)  # Set size and position
        self.add_btn_icon.setPixmap(QtGui.QIcon('add.png').pixmap(50, 50))  # Set icon
        self.add_btn_icon.setScaledContents(True)  # Scale icon to fit the label
        self.add_btn_icon.setCursor(Qt.PointingHandCursor)  # Change cursor to a pointing hand

        # Connect the clicked signal of the QLabel to the on_icon_clicked slot
        self.add_btn_icon.clicked.connect(self.add_btn_clicked)
        self.add_btn_icon.show()

        self.update_btn_icon = ClickableLabel(self.login_window)
        self.update_btn_icon.setGeometry(1125, 175, 50, 50)  # Set size and position
        self.update_btn_icon.setPixmap(QtGui.QIcon('update.png').pixmap(50, 50))  # Set icon
        self.update_btn_icon.setScaledContents(True)  # Scale icon to fit the label
        self.update_btn_icon.setCursor(Qt.PointingHandCursor)  # Change cursor to a pointing hand

        # Connect the clicked signal of the QLabel to the on_icon_clicked slot
        self.update_btn_icon.clicked.connect(self.update_btn_clicked)
        self.update_btn_icon.show()

        self.filter_btn_icon = ClickableLabel(self.login_window)
        self.filter_btn_icon.setGeometry(1125, 250, 50, 50)  # Set size and position
        self.filter_btn_icon.setPixmap(QtGui.QIcon('filter.png').pixmap(50, 50))  # Set icon
        self.filter_btn_icon.setScaledContents(True)  # Scale icon to fit the label
        self.filter_btn_icon.setCursor(Qt.PointingHandCursor)  # Change cursor to a pointing hand

        # Connect the clicked signal of the QLabel to the on_icon_clicked slot
        self.filter_btn_icon.clicked.connect(self.add_btn_clicked)
        self.filter_btn_icon.show()

        self.delete_btn_icon = ClickableLabel(self.login_window)
        self.delete_btn_icon.setGeometry(1125, 325, 50, 50)  # Set size and position
        self.delete_btn_icon.setPixmap(QtGui.QIcon('delete2.png').pixmap(50, 50))  # Set icon
        self.delete_btn_icon.setScaledContents(True)  # Scale icon to fit the label
        self.delete_btn_icon.setCursor(Qt.PointingHandCursor)  # Change cursor to a pointing hand

        # Connect the clicked signal of the QLabel to the on_icon_clicked slot
        self.delete_btn_icon.clicked.connect(self.add_btn_clicked)
        self.delete_btn_icon.show()




    # getting the table dimension
    def get_table(self, query="SELECT * FROM tbl_maintenance WHERE deleted = 'False' ORDER BY control_num DESC"):
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    # create an excel like table object
    def show_table(self):

        self.table = QtWidgets.QTableWidget(self.login_window)

        # Set table size
        self.table.setGeometry(QtCore.QRect(100, 50, 1000, 450))
        self.table.setObjectName("table")
        self.table.setStyleSheet("background-color: white;")
        self.table.verticalHeader().setVisible(False)

        # Fetch table data and column names
        query_result = self.get_table()
        cursor.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_name = 'tbl_maintenance';")  # query for getting the table names
        column_names = ['control_num', 'itemname', 'quantity', 'unit', 'model_name', 'remarks', "deleted", 'encoded_by', 'date_encoded', 'updated_by', 'last_updated']
        self.rows = len(query_result)
        self.columns = len(query_result[0])


        self.table.setColumnCount(self.columns)  # Set number of columns
        self.table.setRowCount(self.rows)  # Set number of rows

        # Populate table with data
        for i in range(self.rows):
            for j in range(self.columns):
                item = QtWidgets.QTableWidgetItem(str(query_result[i][j]))  # Convert to string
                self.table.setItem(i, j, item)

        self.table.setHorizontalHeaderLabels([col.upper() for col in column_names])  # Set column names
        self.table.show()
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def show_selected(self):
        selected = self.table.selectedItems()
        if selected:
            items = [item.text() for item in selected]
            items = items[:self.columns]
            self.selected_values = {
                "ctrl_num": items[0].strip(),
                "itemname": items[1].strip(),
                "quantity": items[2],
                "unit": items[3].strip(),
                "model_name": items[4].strip(),
                "remarks": items[5].strip(),
                "encoded_by": items[7].strip(),
                "date_encoded": items[8].strip(),
                "updated_by": items[9].strip(),
                "last_updated": items[10].strip()

            }
            # show the selected values in the UI



    def parse_inputs(self):

        # Set to None as default if no inputs found
        self.user_inputs = {
            "itemname": self.itemname_box.text().strip(),
            "quantity": self.quantity_box.text().strip(),
            "unit": self.unit_box.text().strip(),
            "model_name": self.model_box.text().strip(),
            "remarks": self.remarks_box.text().strip()
        }

    def clear_inputs(self):
        self.itemname_box.clear()
        self.remarks_box.clear()
        self.unit_box.clear()
        self.quantity_box.clear()
        self.model_box.clear()
        self.table.clearSelection()
        self.show_table()
        self.table.itemSelectionChanged.connect(self.show_selected)

    # Execute when add button is clicked
    def add_btn_clicked(self):


        def click():
            try:
                self.parse_inputs()
                cursor.execute(f"""
                            INSERT INTO tbl_maintenance (itemname, quantity, unit, model_name, remarks)
                            VALUES ('{self.user_inputs["itemname"]}', '{self.user_inputs["quantity"]}', '{self.user_inputs["unit"]}', '{self.user_inputs["model_name"]}', '{self.user_inputs["remarks"]}')

                            """)
                self.conn.commit()
                self.add_window.close()
                self.clear_inputs()
                self.show_table()
                self.table.itemSelectionChanged.connect(self.show_selected)

            except psycopg2.Error as e:
                print(e)
        def cancel():
            self.add_window.close()
            self.show_table()
            self.table.itemSelectionChanged.connect(self.show_selected)


        lbl_font = QtGui.QFont("Arial", 11)
        lbl_font.setBold(True)

        self.add_window = QtWidgets.QWidget()
        self.add_window.setWindowTitle("ADD Data")
        self.add_window.setStyleSheet("background-color : rgba(30,131,177,255)")
        self.add_window.setGeometry(750, 420, 500, 400)
        self.add_window.setFixedSize(450,500)

        #Itemname Box
        self.itemname_box = QtWidgets.QLineEdit(self.add_window)
        self.itemname_box.setGeometry(60, 130, 330, 30)
        self.itemname_box.setFont(QtGui.QFont("Arial", 11))
        self.itemname_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.itemname_box.setAlignment(Qt.AlignCenter)

        #Itemname Label
        self.itemname_label = QtWidgets.QLabel(self.add_window)
        self.itemname_label.setGeometry(65, 168, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Itemname")

        #Quantity Box
        self.quantity_box = QtWidgets.QLineEdit(self.add_window)
        self.quantity_box.setGeometry(60, 190, 100, 30)
        self.quantity_box.setFont(QtGui.QFont("Arial", 11))
        self.quantity_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.quantity_box.setAlignment(Qt.AlignCenter)

        #Quantity Label
        self.itemname_label = QtWidgets.QLabel(self.add_window)
        self.itemname_label.setGeometry(65, 223, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Quantity")

        #Unit Box
        self.unit_box = QtWidgets.QLineEdit(self.add_window)
        self.unit_box.setGeometry(290, 190, 100, 30)
        self.unit_box.setFont(lbl_font)
        self.unit_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.unit_box.setAlignment(Qt.AlignCenter)

        #Unit Label
        self.itemname_label = QtWidgets.QLabel(self.add_window)
        self.itemname_label.setGeometry(320, 223, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Unit")

        #Model box
        self.model_box = QtWidgets.QLineEdit(self.add_window)
        self.model_box.setGeometry(60, 260, 230, 30)
        self.model_box.setFont(QtGui.QFont("Arial", 11))
        self.model_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.model_box.setAlignment(Qt.AlignCenter)

        # Model Label
        self.itemname_label = QtWidgets.QLabel(self.add_window)
        self.itemname_label.setGeometry(65, 293, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Model")

        #Remarks Box
        self.remarks_box = QtWidgets.QLineEdit(self.add_window)
        self.remarks_box.setGeometry(60, 330, 200, 30)
        self.remarks_box.setFont(QtGui.QFont("Arial", 11))
        self.remarks_box.setStyleSheet("background-color: white; border-radius: 10px;")

        # Remarks Label
        self.itemname_label = QtWidgets.QLabel(self.add_window)
        self.itemname_label.setGeometry(65, 360, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Itemname")

        #Add Button
        self.add_btn = QtWidgets.QPushButton(self.add_window)
        self.add_btn.setGeometry(100, 420, 100, 30)
        self.add_btn.setText("Add")
        self.add_btn.setStyleSheet("background-color: white;")
        self.add_btn.clicked.connect(click)

        #cancel button
        self.cancel_btn = QtWidgets.QPushButton(self.add_window)
        self.cancel_btn.setGeometry(270, 420, 100, 30)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.setStyleSheet("background-color: white;")
        self.cancel_btn.clicked.connect(cancel)

        self.add_window.show()



    def update_btn_clicked(self):
        def update():
            try:
                self.parse_inputs()
                cursor.execute(f"""UPDATE tbl_maintenance
                                SET itemname = '{self.user_inputs["itemname"]}', quantity = {self.user_inputs["quantity"]}, 
                                unit = '{self.user_inputs["unit"]}',model_name = '{self.user_inputs["model_name"]}',
                                remarks = '{self.user_inputs["remarks"]}'
                                WHERE control_num = {self.selected_values["ctrl_num"]}
                                """)
                for key,value in self.selected_values.items():
                    print(key,value)


                self.conn.commit()
                self.updt_window.close()
                self.clear_inputs()
                self.show_table()
                self.table.itemSelectionChanged.connect(self.show_selected)


            except Exception as e:
                print(e)
                self.clear_inputs()
                self.show_table()

        def cancel():
            self.updt_window.close()
            self.show_table()
            self.table.itemSelectionChanged.connect(self.show_selected)



        lbl_font = QtGui.QFont("Arial", 11)
        lbl_font.setBold(True)

        self.updt_window = QtWidgets.QWidget()
        self.updt_window.setWindowTitle("Update Data")
        self.updt_window.setStyleSheet("background-color : rgba(30,131,177,255)")
        self.updt_window.setGeometry(750, 420, 500, 400)
        self.updt_window.setFixedSize(450, 500)

        #Itemname Box
        self.itemname_box = QtWidgets.QLineEdit(self.updt_window)
        self.itemname_box.setGeometry(60, 130, 330, 30)
        self.itemname_box.setFont(QtGui.QFont("Arial", 11))
        self.itemname_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.itemname_box.setAlignment(Qt.AlignCenter)

        #Itemname Label
        self.itemname_label = QtWidgets.QLabel(self.updt_window)
        self.itemname_label.setGeometry(65, 168, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Itemname")

        # Quantity Box
        self.quantity_box = QtWidgets.QLineEdit(self.updt_window)
        self.quantity_box.setGeometry(60, 190, 100, 30)
        self.quantity_box.setFont(QtGui.QFont("Arial", 11))
        self.quantity_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.quantity_box.setAlignment(Qt.AlignCenter)

        # Quantity Label
        self.itemname_label = QtWidgets.QLabel(self.updt_window)
        self.itemname_label.setGeometry(65, 223, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Quantity")

        # Unit Box
        self.unit_box = QtWidgets.QLineEdit(self.updt_window)
        self.unit_box.setGeometry(290, 190, 100, 30)
        self.unit_box.setFont(lbl_font)
        self.unit_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.unit_box.setAlignment(Qt.AlignCenter)

        # Unit Label
        self.itemname_label = QtWidgets.QLabel(self.updt_window)
        self.itemname_label.setGeometry(320, 223, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Unit")

        # Model box
        self.model_box = QtWidgets.QLineEdit(self.updt_window)
        self.model_box.setGeometry(60, 260, 230, 30)
        self.model_box.setFont(QtGui.QFont("Arial", 11))
        self.model_box.setStyleSheet("background-color: white; border-radius: 10px;")
        self.model_box.setAlignment(Qt.AlignCenter)

        # Model Label
        self.itemname_label = QtWidgets.QLabel(self.updt_window)
        self.itemname_label.setGeometry(65, 293, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Model")

        # Remarks Box
        self.remarks_box = QtWidgets.QLineEdit(self.updt_window)
        self.remarks_box.setGeometry(60, 330, 200, 30)
        self.remarks_box.setFont(QtGui.QFont("Arial", 11))
        self.remarks_box.setStyleSheet("background-color: white; border-radius: 10px;")

        # Remarks Label
        self.itemname_label = QtWidgets.QLabel(self.updt_window)
        self.itemname_label.setGeometry(65, 360, 100, 18)
        self.itemname_label.setStyleSheet("color: black")
        self.itemname_label.setFont(lbl_font)
        self.itemname_label.setText("Itemname")

        # Update Button
        self.update_btn = QtWidgets.QPushButton(self.updt_window)
        self.update_btn.setGeometry(100, 420, 100, 30)
        self.update_btn.setText("Update")
        self.update_btn.setStyleSheet("background-color: white;")
        self.update_btn.clicked.connect(update)

        # cancel button
        self.cancel_btn = QtWidgets.QPushButton(self.updt_window)
        self.cancel_btn.setGeometry(270, 420, 100, 30)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.setStyleSheet("background-color: white;")
        self.cancel_btn.clicked.connect(cancel)

        # set the selected value to the box
        self.itemname_box.setText(self.selected_values["itemname"])
        self.quantity_box.setText(self.selected_values["quantity"])
        self.unit_box.setText(self.selected_values["unit"])
        self.model_box.setText(self.selected_values["model_name"])
        self.remarks_box.setText(self.selected_values["remarks"])

        self.table.itemSelectionChanged.connect(self.show_selected)

        self.updt_window.show()



    def search_btn_clicked(self):
        try:
            self.parse_inputs()
            # Create a list of tuple condition query
            querycon_list = []
            for i, j in self.user_inputs.items():
                if j == "":
                    pass
                else:
                    querycon_list.append((i, j))

            query_con = ""

            for items in querycon_list:
                if len(querycon_list) > 1:
                    if items[0] == "itemname" or items != querycon_list[-1]:
                        query_con = (query_con + items[0] + " ILIKE" + " '%" + items[1] + "%'" +
                                     " AND ")
                    elif items == querycon_list[-1]:
                        query_con = query_con + items[0] + " = " + "'" + items[1] + "'"
                    else:
                        query_con = query_con + items[0] + " = " + "'" + items[1] + "'" + " AND "

                else:
                    if items[0] == "itemname":
                        query_con = (query_con + items[0] + " ILIKE" + " '%" + items[1] + "%'")
                    else:
                        query_con = query_con + items[0] + " = " + "'" + items[1] + "'"

            print(query_con)

            cursor.execute(f"""
            SELECT * FROM tbl_maintenance
            WHERE {query_con}
            """)

            # Fetch search results
            search_results = cursor.fetchall()

            # Clear table widget
            self.table.clearContents()

            if not search_results:
                # If no results found, inform the user
                QtWidgets.QMessageBox.information(self.login_window, "No Results",
                                                  "No items found matching the search criteria.")
                self.show_table()
                self.table.itemSelectionChanged.connect(self.show_selected)
            else:
                # Update table with search results
                self.rows = len(search_results)
                self.columns = len(search_results[0])
                self.table.setRowCount(self.rows)
                self.table.setColumnCount(self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        item = QtWidgets.QTableWidgetItem(str(search_results[i][j]))
                        self.table.setItem(i, j, item)

                # Update selection behavior
                self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


        except Exception as e:

            # Handle the error, e.g., inform the user or log the error
            print(e)
            QtWidgets.QMessageBox.critical(self.login_window, "No Results",
                                           f"No items found matching the search criteria.")
            self.conn.rollback()
            self.show_table()

    # Delete single selected line
    def delete_btn_clicked(self):

        try:
            self.parse_inputs()
            cursor.execute(f"""
            UPDATE tbl_maintenance
            SET deleted = 'True'
            WHERE control_num = '{self.selected_values["ctrl_num"]}'

            """)
            self.conn.commit()
            self.clear_inputs()
            self.show_table()
            self.table.itemSelectionChanged.connect(self.show_selected)

        except Exception as e:
            print(e)

    def updateDateTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.formattedDateTime = self.currentDateTime.toString("yyyy-MM-dd hh:mm:ss")
        self.date_label.setText(self.formattedDateTime)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())