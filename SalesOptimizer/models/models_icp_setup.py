from PySide6.QtWidgets import QWidget, QComboBox, QSizePolicy, QTableWidgetItem, QHeaderView, QMessageBox, QTableWidget, QAbstractItemView
from PySide6.QtCore import Qt
from views.py.ui_icp_setup import Ui_icp_setup
from DB.db_connection import db_connection
import mysql.connector

class icpsetup(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_icp_setup()
        self.ui.setupUi(self)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(self.find_main_layout())

        self.setWindowFlag(Qt.Window)
        self.setWindowTitle("ICP Setup")
        self.resize(800, 600)

        # Initialize DB connection
        self.conn = db_connection().conn
        self.cursor = self.conn.cursor(dictionary=True)

        self.original_weights = {}

        # Set up the table and combo
        self.setup_table()
        self.populate_combo()

        # Connect signals and slots
        self.ui.add_combo.currentIndexChanged.connect(self.add_attribute_to_table)
        self.ui.assign_checkbox.stateChanged.connect(self.assign_equal_weights)
        self.ui.define_btn.clicked.connect(self.save_weights)
        self.ui.attribute_tbl.cellChanged.connect(self.validate_weights)

    def find_main_layout(self):
        """Automatically find and return the main layout from the UI."""
        for layout_name in ["gridLayout", "verticalLayout", "horizontalLayout", "formLayout"]:
            layout = getattr(self.ui, layout_name, None)
            if layout:
                return layout
        return None

    def setup_table(self):
        """Set up the table for displaying attributes and weights."""
        table = self.ui.attribute_tbl
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["AttributeID", "Attribute", "Weightage(%)"])
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.setColumnHidden(0, True)  # Hide the 'AttributeID' column completely

        # Set up editing triggers for the table
        table.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_combo(self):
        """Populate the combo box with attribute names from the database."""
        self.cursor.execute("SELECT attribute FROM icp")
        attributes = [row["attribute"] for row in self.cursor.fetchall()]
        self.ui.add_combo.clear()  # Clear previous entries
        self.ui.add_combo.addItem("-- Select Attribute --")  # Default item
        self.ui.add_combo.addItems(attributes)  # Add attributes from DB

    def add_attribute_to_table(self, index):
        """Add the selected attribute to the table if not already added."""
        if index == 0:
            return  # Skip if default option is selected

        attribute = self.ui.add_combo.currentText()
        table = self.ui.attribute_tbl

        # Check if the attribute already exists in the table
        for row in range(table.rowCount()):
            if table.item(row, 1).text() == attribute:
                return  # Attribute already exists, so we do not add it again

        # Fetch attribute data (attribute_id and weight) from DB
        self.cursor.execute("SELECT attribute_id, weight FROM icp WHERE attribute = %s", (attribute,))
        row = self.cursor.fetchone()
        if not row:
            return  # If no row is returned, return early

        attribute_id = row["attribute_id"]
        weight = row["weight"]

        # Add the attribute to the table
        row_index = table.rowCount()
        table.insertRow(row_index)

        # Create and add the cells to the table
        item_id = QTableWidgetItem(str(attribute_id))
        item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Disable editing of the ID
        table.setItem(row_index, 0, item_id)

        item_attr = QTableWidgetItem(attribute)
        item_attr.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Disable editing of the attribute name
        table.setItem(row_index, 1, item_attr)

        item_weight = QTableWidgetItem(str(weight))
        item_weight.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)  # Allow editing of the weight
        table.setItem(row_index, 2, item_weight)

        self.original_weights[attribute_id] = weight
        self.validate_weights()  # Revalidate weights whenever a new row is added

    def assign_equal_weights(self, state):
        table = self.ui.attribute_tbl
        row_count = table.rowCount()
        if row_count == 0:
            return

        equal_weight = round(1.0 / row_count, 4)
        for row in range(row_count):
            item = QTableWidgetItem(f"{equal_weight:.4f}")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 2, item)

        # Set the edit triggers correctly using QAbstractItemView constants
        if state == Qt.Checked:
            table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        else:
            table.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)

        self.validate_weights()

    def validate_weights(self):
        """Validate that all weights are between 0 and 1, and the total weight equals 1."""
        table = self.ui.attribute_tbl
        total = 0.0
        valid = True
        for row in range(table.rowCount()):
            try:
                value = float(table.item(row, 2).text())
                if not (0.0 <= value <= 1.0):
                    valid = False
                    break
                total += value
            except:
                valid = False
                break

        total = round(total, 4)
        define_enabled = valid and total == 1.0000
        self.ui.define_btn.setEnabled(define_enabled)

    def save_weights(self):
        table = self.ui.attribute_tbl
        updates = []
        is_weight_correct = True

        for row in range(table.rowCount()):
            attr_id = int(table.item(row, 0).text())
            new_weight = float(table.item(row, 2).text())

            # Check if the new weight is different from the original weight
            if attr_id not in self.original_weights or round(new_weight, 4) != round(self.original_weights[attr_id], 4):
                updates.append((new_weight, attr_id))
            else:
                # If weight matches the original, we check if it's still correct
                self.cursor.execute("SELECT weight FROM icp WHERE attribute_id = %s", (attr_id,))
                db_weight = self.cursor.fetchone()
                if db_weight and round(new_weight, 4) != round(db_weight["weight"], 4):
                    is_weight_correct = False

        # If no updates are made and weights are already correct, proceed to the next page
        if not updates and is_weight_correct:
            QMessageBox.information(self, "No Changes", "Weights are already correct. Moving to the next page.")
            self.ui.stackedWidget.setCurrentIndex(1)
            return

        # If there are updates, proceed to update the database
        if not updates:
            QMessageBox.information(self, "No Changes", "No weight changes to save.")
            return

        try:
            self.cursor.executemany("UPDATE icp SET weight = %s WHERE attribute_id = %s", updates)
            self.conn.commit()
            QMessageBox.information(self, "Success", "Weights saved successfully.")
            self.ui.stackedWidget.setCurrentIndex(1)
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Failed to update weights: {err}")

