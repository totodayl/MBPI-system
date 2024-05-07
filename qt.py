from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import pandas as pd
import datetime as dt


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
        self.login_window.setStyleSheet("background-color: rgb(165, 200, 255)")
        # Setting the size and position of the main window
        LoginWindow.setFixedSize(1200, 900)  # fixed size
        LoginWindow.move(360, 100)

        # add the table to the Window
        self.show_table()
        self.table.itemSelectionChanged.connect(self.show_selected)  # Selection updates
        # Itemname textbox
        self.itemname_box = QtWidgets.QLineEdit(self.login_window)
        self.itemname_box.setGeometry(QtCore.QRect(100, 520, 190, 30))
        self.itemname_box.setStyleSheet("background-color: white;")
        self.itemname_box.setFont(QtGui.QFont("Arial", 11))
        self.itemname_box.setAutoFillBackground(False)
        self.itemname_box.show()

        # Itemname Label
        self.itemname_label = QtWidgets.QLabel(self.login_window)
        self.itemname_label.setText("Item Name")
        self.itemname_label.setGeometry(QtCore.QRect(155, 550, 100, 30))
        self.itemname_label.setAutoFillBackground(False)
        self.itemname_label.setFont(QtGui.QFont("Arial", 11))
        self.itemname_label.show()

        # Quantity textbox
        self.quantity_box = QtWidgets.QLineEdit(self.login_window)
        self.quantity_box.setGeometry(QtCore.QRect(340, 520, 70, 30))
        self.quantity_box.setStyleSheet("background-color: white;")
        self.quantity_box.setFont(QtGui.QFont("Arial", 11))
        self.quantity_box.setAutoFillBackground(False)
        self.quantity_box.show()

        # Quantity Label
        self.quantity_label = QtWidgets.QLabel(self.login_window)
        self.quantity_label.setText("Quantity")
        self.quantity_label.setGeometry(QtCore.QRect(345, 550, 70, 30))
        self.quantity_label.setAutoFillBackground(False)
        self.quantity_label.setFont(QtGui.QFont("Arial", 11))
        self.quantity_label.show()

        # Unit textbox
        self.unit_box = QtWidgets.QLineEdit(self.login_window)
        self.unit_box.setGeometry(QtCore.QRect(460, 520, 70, 30))
        self.unit_box.setStyleSheet("background-color: white;")
        self.unit_box.setFont(QtGui.QFont("Arial", 11))
        self.unit_box.setAutoFillBackground(False)
        self.unit_box.show()

        # Unit Label
        self.unit_label = QtWidgets.QLabel(self.login_window)
        self.unit_label.setText("Unit")
        self.unit_label.setGeometry(QtCore.QRect(480, 550, 70, 30))
        self.unit_label.setAutoFillBackground(False)
        self.unit_label.setFont(QtGui.QFont("Arial", 11))
        self.unit_label.show()

        # model textbox
        self.model_box = QtWidgets.QLineEdit(self.login_window)
        self.model_box.setGeometry(QtCore.QRect(600, 520, 190, 30))
        self.model_box.setStyleSheet("background-color: white;")
        self.model_box.setFont(QtGui.QFont("Arial", 10))
        self.model_box.setAutoFillBackground(False)
        self.model_box.show()

        # model label
        self.model_label = QtWidgets.QLabel(self.login_window)
        self.model_label.setText("Model")
        self.model_label.setGeometry(QtCore.QRect(680, 550, 70, 30))
        self.model_label.setAutoFillBackground(False)
        self.model_label.setFont(QtGui.QFont("Arial", 11))
        self.model_label.show()

        # remarks textbox
        self.remarks_box = QtWidgets.QLineEdit(self.login_window)
        self.remarks_box.setGeometry(QtCore.QRect(850, 520, 190, 30))
        self.remarks_box.setStyleSheet("background-color: white;")
        self.remarks_box.setFont(QtGui.QFont("Arial", 10))
        self.remarks_box.setAutoFillBackground(False)
        self.remarks_box.show()

        # remarks label
        self.remarks_label = QtWidgets.QLabel(self.login_window)
        self.remarks_label.setText("Remarks")
        self.remarks_label.setGeometry(QtCore.QRect(920, 550, 70, 30))
        self.remarks_label.setAutoFillBackground(False)
        self.remarks_label.setFont(QtGui.QFont("Arial", 11))
        self.remarks_label.show()

        # This part below is for showing logs

        # Encoded By Label
        self.encoded_by = QtWidgets.QLabel(self.login_window)
        self.encoded_by.setText("Encoded By: ")
        self.encoded_by.setGeometry(QtCore.QRect(100, 700, 400, 25))
        self.encoded_by.setAutoFillBackground(False)
        self.encoded_by.setFont(QtGui.QFont("Arial", 12))
        self.encoded_by.setStyleSheet('color: red')
        self.encoded_by.show()

        # Encoded Date Label
        self.encoded_date = QtWidgets.QLabel(self.login_window)
        self.encoded_date.setText("Date Encoded: ")
        self.encoded_date.setGeometry(QtCore.QRect(100, 723, 400, 25))
        self.encoded_date.setAutoFillBackground(False)
        self.encoded_date.setFont(QtGui.QFont("Arial", 12))
        self.encoded_date.setStyleSheet('color: red')
        self.encoded_date.show()

        # Updated By Label
        self.updated_by = QtWidgets.QLabel(self.login_window)
        self.updated_by.setText("Updated By: ")
        self.updated_by.setGeometry(QtCore.QRect(100, 746, 400, 25))
        self.updated_by.setAutoFillBackground(False)
        self.updated_by.setFont(QtGui.QFont("Arial", 12))
        self.updated_by.setStyleSheet('color: red')
        self.updated_by.show()

        # Date Updated Label
        self.updated_date = QtWidgets.QLabel(self.login_window)
        self.updated_date.setText("Updated By: ")
        self.updated_date.setGeometry(QtCore.QRect(100, 769, 400, 25))
        self.updated_date.setAutoFillBackground(False)
        self.updated_date.setFont(QtGui.QFont("Arial", 12))
        self.updated_date.setStyleSheet('color: red')
        self.updated_date.show()

        # Added Buttons

        # Insert Button
        self.insert_btn = QtWidgets.QPushButton(self.login_window)
        self.insert_btn.setText("Add")
        self.insert_btn.setGeometry(QtCore.QRect(850, 700, 100, 50))
        self.insert_btn.clicked.connect(self.add_btn_clicked)
        self.insert_btn.show()

        # Update Button
        self.update_btn = QtWidgets.QPushButton(self.login_window)
        self.update_btn.setText("Update")
        self.update_btn.setGeometry(QtCore.QRect(1000, 700, 100, 50))
        self.update_btn.clicked.connect(self.update_btn_clicked)
        self.update_btn.show()

        # Delete Button
        self.delete_btn = QtWidgets.QPushButton(self.login_window)
        self.delete_btn.setText("Delete")
        self.delete_btn.setGeometry(QtCore.QRect(850, 780, 100, 50))
        self.delete_btn.clicked.connect(self.delete_btn_clicked)
        self.delete_btn.show()

        # Search Button
        self.search_btn = QtWidgets.QPushButton(self.login_window)
        self.search_btn.setText("Search")
        self.search_btn.setGeometry(QtCore.QRect(1000, 780, 100, 50))
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.search_btn.show()

        # Clear Button
        self.clear_btn = QtWidgets.QPushButton(self.login_window)
        self.clear_btn.setText("Clear")
        self.clear_btn.setGeometry(QtCore.QRect(700, 780, 100, 50))
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.clear_btn.show()

        # Date Label
        self.date_label = QtWidgets.QLabel(self.login_window)
        self.date_label.setGeometry(QtCore.QRect(1000, 10, 150, 20))
        self.date_label.setStyleSheet("background-color: white")
        self.date_label.show()

        self.timer = QtCore.QTimer(self.login_window)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)

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
        column_names = ['control_num', 'itemname', 'quantity', 'unit', 'model_name', 'remarks', 'encoded_by', 'date_encoded', 'updated_by', 'last_updated']
        print(column_names)
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
            self.clicked_values = {
                "ctrl_num": items[0],
                "item_name": items[1],
                "quantity": str(items[2]),
                "unit": items[3],
                "model_name": items[4],
                "remarks": items[5],
                "encoded_by": items[7],
                "date_encoded": items[8],
                "updated_by": items[9],
                "last_updated": items[10]

            }
            # show the selected values in the UI
            itemname = self.itemname_box.setText(self.clicked_values["item_name"])
            quantity = self.quantity_box.setText(self.clicked_values["quantity"])
            unit = self.unit_box.setText(self.clicked_values["unit"])
            model = self.model_box.setText(self.clicked_values["model_name"])
            remark = self.remarks_box.setText(self.clicked_values["remarks"])

            self.encoded_by.setText(f"Encoded By: {self.clicked_values['encoded_by']}")
            self.encoded_date.setText(f"Date Encoded: {self.clicked_values['date_encoded']}")
            self.updated_by.setText(f"Updated By: {self.clicked_values['updated_by']}")
            self.updated_date.setText(f"Last Update: {self.clicked_values['last_updated']}")

    def parse_inputs(self):

        # Set to None as default if no inputs found
        self.user_inputs = {
            "itemname": self.itemname_box.text(),
            "quantity": self.quantity_box.text(),
            "unit": self.unit_box.text(),
            "model_name": self.model_box.text(),
            "remarks": self.remarks_box.text()
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
        try:

            self.parse_inputs()
            cursor.execute(f"""
            INSERT INTO tbl_maintenance(itemname, quantity, unit, model_name, remarks,encoded_by, date_encoded)
            VALUES('{self.user_inputs["itemname"]}', '{self.user_inputs["quantity"]}', '{self.user_inputs["unit"]}', 
                   '{self.user_inputs["model_name"]}', '{self.user_inputs["remarks"]}','admin', '{dt.datetime.now()}')

            """)
            self.conn.commit()
            self.clear_inputs()
            self.show_table()
            self.table.itemSelectionChanged.connect(self.show_selected)
            self.itemname_box.setFocus()

        except psycopg2.Error as e:
            print(e)
            QtWidgets.QMessageBox.critical(self.login_window, "Invalid Entry",
                                           f"Missing some inputs")
            self.conn.rollback()
            self.clear_inputs()
            self.show_table()
            self.table.itemSelectionChanged.connect(self.show_selected)

    def update_btn_clicked(self):
        try:
            id = self.clicked_values["ctrl_num"]
            self.parse_inputs()
            if self.user_inputs["itemname"] == None or self.user_inputs["quantity"] == None or self.user_inputs[
                "model_name"] == None:
                QtWidgets.QMessageBox.critical(self.login_window, "Cannot be Null",
                                               "Item Name, Quantity and Model Name cannot be empty")

            else:
                try:
                    int(self.user_inputs["quantity"])
                    cursor.execute(f"""
                                                                            UPDATE tbl_maintenance
                                                                            SET itemname = '{self.user_inputs["itemname"]}',
                                                                            quantity = '{"NULL" if self.user_inputs["quantity"] == "" else self.user_inputs["quantity"]}', 
                                                                            unit = '{"NULL" if self.user_inputs["unit"] == "" else self.user_inputs["unit"]}', 
                                                                            model_name = '{"NULL" if self.user_inputs["model_name"] == "" else self.user_inputs["model_name"]}', 
                                                                            remarks = '{"NULL" if self.user_inputs["remarks"] == "" else self.user_inputs["remarks"]}',
                                                                            encoded_by = 'admin'
                                                                            WHERE control_num = {id}
                                                                            """)
                    self.conn.commit()
                    self.clear_inputs()
                    self.show_table()
                    self.table.itemSelectionChanged.connect(self.show_selected)
                except:
                    QtWidgets.QMessageBox.critical(self.login_window, "Invalid Data", "Quantity only accepts Integer")

        except Exception as e:
            print(e)
            self.conn.rollback()
            self.clear_inputs()
            self.show_table()
            self.table.itemSelectionChanged.connect(self.show_selected)

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
            print(querycon_list)

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
            WHERE control_num = '{self.clicked_values["ctrl_num"]}'

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
