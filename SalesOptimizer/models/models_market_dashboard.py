from views.py.ui_market_dashboard import Ui_Form
from Data.Lead_Data import Lead_Data

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys, datetime

#A. PVLS = Prospects vs Lead Score

class marketdashboard(QWidget, Ui_Form):

    # -------------------------- Main Window content
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        


        dog = Lead_Data()
        self.ProspectsVsLeadScore = dog.getLeadCountPerScore()
        self.LeadOverTime = dog.getLeadOverTimeData()
        self.SalesWonCost = dog.getOpportunityWonCostOverLeadScore()
        self.Opportunities = dog.getOpportunityStatusPerLeadScore()
        print(self.Opportunities)

        self.leadOverTime_comboBox.currentIndexChanged.connect(self.loadFigureLeadsOverTime)
        self.RevenueOverLeadScore_comboBox.currentTextChanged.connect(self.loadFigureSalesWonVsLeadScore)

        #self.loadFigureLeadsOverTime()
        self.loadFigureProspectsVsLeadScore()
        self.loadFigureConversionVsLeadScore()
        #self.loadFigureSalesWonVsLeadScore()
        self.loadFigureTotalScoreVsLeadScore()

    def loadFigureLeadsOverTime(self, Days):
        # Create figure before using it
        fig = Figure()
        ax = fig.add_subplot()

        print("Days : ",Days)
        day = 7

        if Days == 0:
            # A Week Ago
            day = 7
        elif Days == 1:
            # A Month Ago
            day = 30
        elif Days == 2:
            day = 120
        elif Days == 3:
            day = 365


        # Get today's date
        today = datetime.date.today()

        # Get the date 7 days ago
        n_days_ago = today - datetime.timedelta(days=day)

        # Initialize the lead and time variables as empty lists
        lead = []
        time = []

        # Loop through each tuple in the leadovertime list
        for date, count in self.LeadOverTime:
            if date >= n_days_ago:  # Check if the date is within the last 7 days
                lead.append(count)  # Extract the lead count
                time.append(date.strftime("%B %d, %Y"))

        for i in reversed(range(self.LVT_gridLayout.count())):
            widget = self.LVT_gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()  # Remove and delete widget


        # Plot lead vs time data
        ax.plot(time, lead, marker='o', linestyle='-', color='b')

        # Set axis labels
        ax.set_xlabel('Date')  # Label for lead
        ax.set_ylabel('Number of Leads')  # Label for time

        # Set title
        ax.set_title('Lead vs Time')

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.LVT_gridLayout.addWidget(canvas)  # Add canvas to layout

            # Draw figure (important)
        canvas.draw()

        # Now tight layout after drawing
        fig.tight_layout()

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

    # Check
    def loadFigureProspectsVsLeadScore(self):
        fig = Figure(figsize=(6, 4))  # only set size (w, h)
        ax = fig.add_subplot()

        lead_data = self.ProspectsVsLeadScore

        # Expand into flat list for histogram
        data = []
        for score, count in lead_data:
            data.extend([score] * count)


        # Plot
        bars = ax.hist(data, bins=10, rwidth=0.95)

        ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
        ax.set_title("Current Number of Prospects in Lead Score")
        ax.set_xlabel('Lead Score')
        ax.set_ylabel('Number of Prospects')


        # Alternate bar colors between blue and green
        for idx, bar in enumerate(bars[2]):  # bars[2] are the individual bar containers
            if idx % 2 == 0:
                bar.set_facecolor('blue')
            else:
                bar.set_facecolor('green')

            # Add text label above each bar with the count
            height = bar.get_height()  # Get the height of the bar (the count)
            ax.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)),
            ha='center', va='bottom', fontsize=10, color='black')

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

    
    def loadFigureSalesWonVsLeadScore(self, Days):
        fig = Figure(figsize=(6, 4))  # only set size (width, height)
        ax = fig.add_subplot()
        

        print("Days : ",Days)
        day = 7

        if Days == 0:
            # A Week Ago
            day = 7
        elif Days == 1:
            # A Month Ago
            day = 30
        elif Days == 2:
            day = 120
        elif Days == 3:
            day = 365


        data = self.SalesWonCost
        Lead_Score = [score for score, _ in data]
        Sales_Revenue = [cost for _, cost in data]

        # Plot bars manually
        bars = ax.bar(Lead_Score, Sales_Revenue, width=0.8)

        ax.set_xticks(Lead_Score)
        ax.set_xlabel('Lead Score')
        ax.set_ylabel('Sales Revenue₱')

        # Alternate bar colors between blue and green
        for idx, bar in enumerate(bars):
            if idx % 2 == 0:
                bar.set_facecolor('blue')
            else:
                bar.set_facecolor('green')


        for i in reversed(range(self.SWVLS_gridLayout.count())):
            widget = self.SWVLS_gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()  # Remove and delete widget

        # Create and add canvas
        canvas = FigureCanvas(fig)
        self.SWVLS_gridLayout.addWidget(canvas)



        # Add text labels above each bar
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:,.0f}",
                ha='center',
                va='bottom',
                fontsize=8,
                color='black'
            )

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

        
        # Separate the data
        Owon, Oloss = self.Opportunities  # Owon and Oloss are both lists of (lead_score, count)

        # Sample data for Total Leads with three categories: Won, Lost, Pending Opportunities
        lead_score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example months

        # Initialize won and lost with just the counts
        won = [count for _, count in Owon]
        lost = [count for _, count in Oloss]
        pending = [0,0,0,0,0,0,0,0,0,0]  # Pending opportunities

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


        # Annotate values on bars
        for i in range(len(lead_score)):
            y_won = won[i]
            y_lost = lost[i]
            y_pending = pending[i]

            x = lead_score[i]

            if y_won > 0:
                ax.text(x, y_won / 2, str(y_won), ha='center', va='center', color='white', fontsize=8)

            if y_lost > 0:
                ax.text(x, y_won + y_lost / 2, str(y_lost), ha='center', va='center', color='white', fontsize=8)

            if y_pending > 0:
                ax.text(x, y_won + y_lost + y_pending / 2, str(y_pending), ha='center', va='center', color='black', fontsize=8)


        # Draw the figure (important)
        canvas.draw()

        # Tight layout after drawing
        fig.tight_layout(pad=3.0)
