from views.py.ui_market_dashboard import Ui_Form

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys

#A. PVLS = Prospects vs Lead Score

class marketdashboard(QWidget, Ui_Form):

    # -------------------------- Main Window content
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loadFigurePVLS()
        self.loadFigureCVLS()
        self.loadFigureSWVLS()
        self.loadFigureTSVLS()


    def loadFigurePVLS(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Plot your data
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        ax.plot(x, y)

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.PVLS_gridLayout.addWidget(canvas)   # add canvas to layout

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.PVLS_gridLayout.addWidget(toolbar)

    def loadFigureCVLS(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Plot your data
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        ax.plot(x, y)

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.CVLS_gridLayout.addWidget(canvas)   # add canvas to layout

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.CVLS_gridLayout.addWidget(toolbar)

    def loadFigureSWVLS(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Plot your data
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        ax.plot(x, y)

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.SWVLS_gridLayout.addWidget(canvas)   # add canvas to layout

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.SWVLS_gridLayout.addWidget(toolbar)

    def loadFigureTSVLS(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Plot your data
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        ax.plot(x, y)

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.TSVLS_gridLayout.addWidget(canvas)   # add canvas to layout

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.TSVLS_gridLayout.addWidget(toolbar)