from views.py.ui_market_dashboard import Ui_Form

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
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
        
        self.loadFigureLeadsOverTime()
        self.loadFigureProspectsVsLeadScore()
        self.loadFigureConversionVsLeadScore()
        self.loadFigureSalesWonVsLeadScore()
        self.loadFigureTotalScoreVsLeadScore()

    def loadFigureLeadsOverTime(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Example data for Lead vs Time (modify according to your real data)
        lead = [11, 24, 31, 49, 45, 51, 50, 24, 125, 256]
        time = [1, 2, 3, 4, 5,6,7,8,9,10]  # Replace this with actual time data

        # Plot lead vs time data
        ax.plot(time, lead, marker='o', linestyle='-', color='b')

        # Set axis labels
        ax.set_xlabel('Months')  # Label for lead
        ax.set_ylabel('Number of Leads')  # Label for time

        # Set title
        ax.set_title('Lead vs Time Conversion')

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.LVT_gridLayout.addWidget(canvas)  # Add canvas to layout

            # Draw figure (important)
        canvas.draw()

        # Now tight layout after drawing
        fig.tight_layout(pad=3.0)

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.LVT_gridLayout.addWidget(toolbar)


    
    def loadFigureConversionVsLeadScore(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Plot your data
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        ax.plot(x, y)
        ax.set_title("Current Conversion Rate (%) Per Lead Score Range")
        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.CVLS_gridLayout.addWidget(canvas)   # add canvas to layout

        # Draw figure (important)
        canvas.draw()

        # Now tight layout after drawing
        fig.tight_layout(pad=3.0)


        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.CVLS_gridLayout.addWidget(toolbar)


    def loadFigureProspectsVsLeadScore(self):
        fig = Figure(figsize=(6, 4))  # only set size (w, h)
        ax = fig.add_subplot()

        # Plot
        # The amount of lead score = 10 in a data set
        data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 10]
        bars = ax.hist(data, bins=10, rwidth=0.95)

        ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
        ax.set_title("Total Prospects Per Lead Score Range ")
        ax.set_xlabel('Lead Score')
        ax.set_ylabel('Number of Prospects')


        # Alternate bar colors between blue and green
        for idx, bar in enumerate(bars[2]):  # bars[2] are the individual bar containers
            if idx % 2 == 0:
                bar.set_facecolor('blue')
            else:
                bar.set_facecolor('green')

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.PVLS_gridLayout.addWidget(canvas)

        # Draw figure (important)
        canvas.draw()

        # Now tight layout after drawing
        fig.tight_layout(pad=3.0)

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.PVLS_gridLayout.addWidget(toolbar)

    def loadFigureSalesWonVsLeadScore(self):
        fig = Figure(figsize=(6, 4))  # only set size (width, height)
        ax = fig.add_subplot()

        # Lead Scores (x-axis)
        lead_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Sales Revenue (y-axis)
        sales_revenue = [1000, 2500, 3000, 4500, 2000, 3500, 1500, 4000, 2200, 5000]  # <-- YOUR REAL DATA HERE

        # Plot bars manually
        bars = ax.bar(lead_scores, sales_revenue, width=0.8)

        ax.set_xticks(lead_scores)
        ax.set_xlabel('Lead Score')
        ax.set_ylabel('Sales Revenue')

        # Alternate bar colors between blue and green
        for idx, bar in enumerate(bars):
            if idx % 2 == 0:
                bar.set_facecolor('blue')
            else:
                bar.set_facecolor('green')

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.SWVLS_gridLayout.addWidget(canvas)

        # Draw figure (important)
        canvas.draw()

        # Tight layout
        fig.tight_layout(pad=3.0)

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.SWVLS_gridLayout.addWidget(toolbar)

        
    def loadFigureTotalScoreVsLeadScore(self):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        # Sample data for Total Leads with three categories: Won, Lost, Pending Opportunities
        lead_score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example months
        won = [1, 3, 2, 5, 6, 1, 3, 2, 5, 6]  # Won opportunities
        lost = [0, 2, 4, 3, 1, 1, 3, 2, 5, 6]  # Lost opportunities
        pending = [2, 1, 3, 2, 4, 1, 3, 2, 5, 6]  # Pending opportunities

        # Create stacked bar chart by stacking Won, Lost, Pending on top of each other
        ax.bar(lead_score, won, label='Won', color='green')  # Bottom of the bar for Won
        ax.bar(lead_score, lost, bottom=won, label='Lost', color='red')  # Stack Lost on top of Won
        ax.bar(lead_score, pending, bottom=[i+j for i,j in zip(won, lost)], label='Pending', color='yellow')  # Stack Pending on top of Won + Lost

        # Set axis labels
        ax.set_xlabel('Lead Score')
        ax.set_ylabel('Opportunities')

        # Add a legend
        ax.legend()

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.TSVLS_gridLayout.addWidget(canvas)   # Add canvas to layout

        # Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.TSVLS_gridLayout.addWidget(toolbar)

        # Draw the figure (important)
        canvas.draw()

        # Tight layout after drawing
        fig.tight_layout(pad=3.0)
