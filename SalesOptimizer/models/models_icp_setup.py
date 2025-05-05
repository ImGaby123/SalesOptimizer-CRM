from PySide6.QtWidgets import QWidget, QComboBox, QSizePolicy, QTableWidgetItem, QHeaderView, QMessageBox, QTableWidget, QAbstractItemView
from PySide6.QtWidgets import (
    QScrollArea, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QSpacerItem
)
from PySide6.QtCore import Qt
from views.py.ui_icp_setup import Ui_icp_setup
from DB.db_connection import db_connection
from DB.db_functions import db_functions

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

        # Initialize DB connection and functions
        self.db = db_functions(db_connection())

        self.original_weights = {}

        # Page 1 setup
        self.setup_table()
        self.populate_combo()

        self.ui.add_combo.currentIndexChanged.connect(self.add_attribute_to_table)
        self.ui.assign_checkbox.stateChanged.connect(self.assign_equal_weights)
        self.ui.define_btn.clicked.connect(self.save_weights)
        self.ui.attribute_tbl.cellChanged.connect(self.validate_weights)

        # Page 2 setup
        self.setup_second_page()

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
        attributes = self.db.get_attributes()
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

        attribute_data = self.db.get_attribute_data(attribute)
        if not attribute_data:
            return  # If no row is returned, return early

        attribute_id = attribute_data["attribute_id"]
        weight = attribute_data["weight"]

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

            if attr_id not in self.original_weights or round(new_weight, 4) != round(self.original_weights[attr_id], 4):
                updates.append((new_weight, attr_id))
            else:
                self.cursor.execute("SELECT weight FROM icp WHERE attribute_id = %s", (attr_id,))
                db_weight = self.cursor.fetchone()
                if db_weight and round(new_weight, 4) != round(db_weight["weight"], 4):
                    is_weight_correct = False

        if not updates and is_weight_correct:
            QMessageBox.information(self, "No Changes", "Weights are already correct. Moving to the next page.")
            self.ui.stackedWidget.setCurrentIndex(1)
            return

        if not updates:
            QMessageBox.information(self, "No Changes", "No weight changes to save.")
            return

        try:
            self.db.update_weight(updates)
            QMessageBox.information(self, "Success", "Weights saved successfully.")
            self.ui.stackedWidget.setCurrentIndex(1)
        except Exception as err:
            QMessageBox.critical(self, "Database Error", f"Failed to update weights: {err}")

    def setup_second_page(self):
        self.active_attribute_id = None
        self.dynamic_entries = []
        self.score_choices = [str(i) for i in range(1, 11)]

        self.scroll_container = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_container)
        self.ui.scroll_area.setWidget(self.scroll_container)
        self.ui.scroll_area.setWidgetResizable(True)

        self.populate_attribute_table()
        self.ui.attribute_tbl_2.cellClicked.connect(self.on_attribute_selected)
        self.ui.add_btn.clicked.connect(self.add_rule_input_row)
        self.ui.save_btn.clicked.connect(self.save_rules)

    def populate_attribute_table(self):
        rows = self.db.get_all_attributes()
        self.ui.attribute_tbl_2.setRowCount(len(rows))
        self.ui.attribute_tbl_2.setColumnCount(2)
        self.ui.attribute_tbl_2.setHorizontalHeaderLabels(["ID", "Attribute"])

        for row_index, row_data in enumerate(rows):
            attr_id_item = QTableWidgetItem(str(row_data["attribute_id"]))
            attr_item = QTableWidgetItem(row_data["attribute"])
            self.ui.attribute_tbl_2.setItem(row_index, 0, attr_id_item)
            self.ui.attribute_tbl_2.setItem(row_index, 1, attr_item)

        self.ui.attribute_tbl_2.setColumnHidden(0, True)

    def on_attribute_selected(self, row, _):
        self.clear_rule_inputs()

        table = self.ui.attribute_tbl_2
        self.active_attribute_id = int(table.item(row, 0).text())
        attribute_name = table.item(row, 1).text()
        self.ui.when_lbl.setText(f"When {attribute_name} Contains")

        rules = self.db.get_icp_rules(self.active_attribute_id)
        for rule in rules:
            self.add_rule_input_row(rule["attribute_value"], rule["attribute_score"])

    def clear_rule_inputs(self):
        for widget in self.dynamic_entries:
            widget.setParent(None)
        self.dynamic_entries.clear()

    def add_rule_input_row(self, value_text="", score_value=None):
        row = QWidget()
        layout = QHBoxLayout(row)

        value_input = QLineEdit()
        value_input.setPlaceholderText("Enter value")
        if value_text:
            value_input.setText(str(value_text))

        score_label = QLabel("Score:")
        score_combo = QComboBox()
        score_combo.addItems(self.score_choices)

        if score_value is not None:
            index = score_combo.findText(str(score_value))
            score_combo.setCurrentIndex(index if index >= 0 else 0)

        layout.addWidget(value_input)
        layout.addWidget(score_label)
        layout.addWidget(score_combo)

        # Insert the row at the top of the layout
        self.scroll_layout.insertWidget(0, row)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.scroll_layout.insertItem(1, spacer)

        self.dynamic_entries.insert(0, row)
        row.inputs = (value_input, score_combo)


    def save_rules(self):
        if not self.active_attribute_id:
            QMessageBox.warning(self, "No Attribute", "Please select an attribute.")
            return

        self.db.delete_rules(self.active_attribute_id)

        inserts = []
        for widget in self.dynamic_entries:
            value_input, score_combo = widget.inputs
            value = value_input.text().strip()
            if not value:
                continue
            score = int(score_combo.currentText())

            # Check if the rule already exists before adding it
            existing_rule = self.db.get_rule_by_value(self.active_attribute_id, value, score)
            if existing_rule:
                continue

            inserts.append((self.active_attribute_id, value, score))

        if inserts:
            try:
                self.db.insert_rules(inserts)
                QMessageBox.information(self, "Saved", "Rules saved successfully.")
            except Exception as err:
                QMessageBox.critical(self, "Database Error", f"An error occurred: {err}")
        else:
            QMessageBox.information(self, "No Changes", "No new rules to save.")

