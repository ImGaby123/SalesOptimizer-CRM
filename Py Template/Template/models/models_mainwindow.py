import os
from PySide6.QtWidgets import (QDialog, QMessageBox, QMainWindow, QMdiArea, QMdiSubWindow, QWidget, QMenuBar, QStatusBar, QSizePolicy)
from PySide6.QtGui import QAction, QBrush, QColor
from PySide6.QtCore import Qt, Signal

# Sidebar
from .models_sidebar import SidebarForm

# Items Page
from .models_item_table_view import ItemTableView


current_dir = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window Name
        self.setWindowTitle("System123")


        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        self.mdi_area.setBackground(QBrush(QColor(255, 255, 255)))  # White background

        self.setMenuBar(QMenuBar(self))
        self.setStatusBar(QStatusBar(self))



        self.transposed = False  # Track the state of transposition
        self.sidebar_visible = True  # Track sidebar visibility
        self.create_menu()
        self.create_subwindows()
        self.showMaximized()


# Menu Option Here -----------------------------------------
    def create_menu(self):
        menu_bar = self.menuBar()
        open_menu = menu_bar.addMenu("Open")
        window_menu = menu_bar.addMenu("Window")

        self.sidebar_action = QAction("Sidebar", self, checkable=True)
        self.sidebar_action.setChecked(True)
        self.sidebar_action.triggered.connect(self.toggle_sidebar)

        self.mainform_action = QAction("MainForm", self, checkable=True)
        self.mainform_action.setChecked(True)
        self.mainform_action.triggered.connect(self.toggle_mainform)

        open_menu.addAction(self.sidebar_action)
        open_menu.addAction(self.mainform_action)

        realign_action = QAction("Realign Windows", self)
        realign_action.triggered.connect(self.realign_subwindows)

        transpose_action = QAction("Transpose Windows", self)
        transpose_action.triggered.connect(self.transpose_subwindows)

        window_menu.addAction(realign_action)
        window_menu.addAction(transpose_action)
# ----------------------------------------------------------------------------------


# Create Sub Window Here -----------------------------------------
    def create_subwindows(self):
        screen_width = self.screen().availableGeometry().width()
        screen_height = self.screen().availableGeometry().height() - self.menuBar().height() - self.statusBar().height()

        self.sidebar = SidebarForm()
        self.sidebar.changeForm.connect(self.load_form)

        self.left_subwin = self.create_mdi_subwindow(self.sidebar, int(screen_width * 0.1), screen_height, 0, 0)
        self.right_subwin = self.create_mdi_subwindow(QWidget(), int(screen_width * 0.9), screen_height, int(screen_width * 0.1), 0)
        self.right_subwin.closeEvent = self.handle_right_close
        self.left_subwin.closeEvent = self.handle_left_close
# ----------------------------------------------------------------------------------



# Sidebar buttons Commands Here -----------------------------------------
    def load_form(self, form_name):
        form_dict = {
            "Home": SidebarForm,
            "Item1": ItemTableView,
            "Item2": None
        }

        if form_name not in form_dict or form_dict[form_name] is None:
            QMessageBox.warning(self, "Invalid Action", f"No form assigned for {form_name}.")
            return

        target_subwin = self.right_subwin if not self.transposed else self.left_subwin

        if target_subwin.widget():
            target_subwin.widget().deleteLater()
            target_subwin.setWidget(None)

        form_class = form_dict[form_name]
        new_widget = form_class() if issubclass(form_class, QWidget) else MainForm(form_class)
        target_subwin.setWidget(new_widget)
        target_subwin.show()

# ----------------------------------------------------------------------------------




# Sub Win Configuration Here  -----------------------------------------
    def create_mdi_subwindow(self, widget, width, height, x, y):
        subwin = QMdiSubWindow()
        subwin.setWidget(widget)
        subwin.setWindowTitle("")
        #subwin.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        subwin.setWindowFlags(Qt.Widget | Qt.CustomizeWindowHint)
        subwin.resize(width, height)
        self.mdi_area.addSubWindow(subwin)
        subwin.move(x, y)
        subwin.show()
        return subwin
# ----------------------------------------------------------------------------------



# Sub Win Actions Here  -----------------------------------------
    def realign_subwindows(self):
        screen_width = self.width()
        screen_height = self.height() - self.menuBar().height() - self.statusBar().height()

        if self.sidebar_visible:
            left_width = int(screen_width * 0.1)
            right_width = int(screen_width * 0.9)
        else:
            left_width = 0
            right_width = screen_width

        if self.transposed:
            self.left_subwin.setGeometry(0, 0, right_width, screen_height)
            self.right_subwin.setGeometry(right_width, 0, left_width, screen_height)
        else:
            self.left_subwin.setGeometry(0, 0, left_width, screen_height)
            self.right_subwin.setGeometry(left_width, 0, right_width, screen_height)

    def transpose_subwindows(self):
        self.transposed = not self.transposed  # Toggle transposition state
        self.left_subwin, self.right_subwin = self.right_subwin, self.left_subwin
        self.realign_subwindows()

    def toggle_sidebar(self):
        sidebar_subwin = self.left_subwin if not self.transposed else self.right_subwin

        if self.sidebar_visible:
            sidebar_subwin.hide()
            self.sidebar_visible = False
        else:
            if sidebar_subwin is None or sidebar_subwin.isHidden():  # Ensure sidebar exists & isn't hidden
                sidebar_subwin.show()
                sidebar_subwin.setGeometry(0, 0, int(self.width() * 0.1), self.height())  # Restore sidebar size
                sidebar_subwin.closeEvent = self.handle_left_close  # Reconnect close event if needed

            self.sidebar_visible = True

        self.sidebar_action.setChecked(self.sidebar_visible)
        self.realign_subwindows()

    def toggle_mainform(self):
     if self.right_subwin is not None:
        self.right_subwin.setVisible(not self.right_subwin.isVisible())
        self.mainform_action.setChecked(self.right_subwin.isVisible())

    def handle_left_close(self, event):
        self.sidebar_visible = False
        self.sidebar_action.setChecked(False)

        screen_width = self.width()
        screen_height = self.height() - self.menuBar().height() - self.statusBar().height()

        # Identify which subwindow is actually the sidebar
        sidebar_subwin = self.left_subwin if not self.transposed else self.right_subwin
        mainform_subwin = self.right_subwin if not self.transposed else self.left_subwin

        sidebar_subwin.hide()  # Only hide the sidebar, don't touch mainform

        # Expand the mainform when sidebar is closed
        mainform_subwin.setGeometry(0, 0, screen_width, screen_height)

        self.realign_subwindows()
        event.ignore()  # Prevent actual closing

    def handle_right_close(self, event):
        self.mainform_action.setChecked(False)
        event.accept()

    def resizeEvent(self, event):
        self.realign_subwindows()
        super().resizeEvent(event)
# ----------------------------------------------------------------------------------


class ResizableForm(QWidget):
    def __init__(self, ui_class):
        super().__init__()
        self.ui = ui_class()
        self.ui.setupUi(self)

        # ✅ Allow full expansion
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # ✅ Apply correct layout dynamically
        layout = self.find_main_layout()
        if layout:
            self.setLayout(layout)

    def find_main_layout(self):
        """Automatically detect the main layout in the UI class."""
        for attr_name in ["gridLayout", "verticalLayout", "horizontalLayout", "formLayout"]:
            layout = getattr(self.ui, attr_name, None)
            if layout:
                return layout
        return None  # No layout found, default behavior


class MDIManager:
    @staticmethod
    def load_into_mdi(widget_class):
        from PySide6.QtWidgets import QApplication
        from models.models_mainwindow import MainWindow

        main_window = next((w for w in QApplication.instance().topLevelWidgets() if isinstance(w, MainWindow)), None)
        if not main_window:
            print("Error: MainWindow not found!")
            return

        target_subwin = main_window.right_subwin if not main_window.transposed else main_window.left_subwin
        if target_subwin.widget():
            target_subwin.widget().deleteLater()
            target_subwin.setWidget(None)

        new_widget = widget_class()
        target_subwin.setWidget(new_widget)
        target_subwin.show()
