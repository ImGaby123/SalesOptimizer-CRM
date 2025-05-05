from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Grid Example")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.add_button = QPushButton("Add")
        self.layout.addWidget(self.add_button, 0, 0)

        self.print_button = QPushButton("Print")
        self.layout.addWidget(self.print_button, 100, 0)

        self.add_button.clicked.connect(self.add_row)
        self.print_button.clicked.connect(self.print_all_values)

        self.row_count = 1  # Start adding from row 1
        self.textboxes = []  # Store references to all QLineEdits

    def add_row(self):
        label = QLabel(f"Label {self.row_count}")
        textbox = QLineEdit()
        button = QPushButton("Action")

        self.layout.addWidget(label, self.row_count, 0)
        self.layout.addWidget(textbox, self.row_count, 1)
        self.layout.addWidget(button, self.row_count, 2)

        self.textboxes.append(textbox)

        # Connect this button to print its own textbox value
        button.clicked.connect(lambda _, tb=textbox: print(f"Action: {tb.text()}"))

        self.row_count += 1

    def print_all_values(self):
        print("All Textbox Values:")
        for textbox in self.textboxes:
            print(textbox.text())

if __name__ == "__main__":
    app = QApplication([])
    window = MyForm()
    window.show()
    app.exec()
