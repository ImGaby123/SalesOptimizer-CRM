from views.py.ui_sales_dashboard import Ui_Form
from Data.Lead_Data import Lead_Data

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# Prophet
import pandas as pd
from prophet import Prophet
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


import sys, datetime

#A. PVLS = Prospects vs Lead Score

class salesdashboard(QWidget, Ui_Form):

    # -------------------------- Main Window content
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        dog = Lead_Data()
        self.saleWonRevenue = dog.getSaleCost()
        print(self.saleWonRevenue)
        self.SG_pushButton.clicked.connect(self.loadFigureSalesWon)
        self.SG_pushButton_2.clicked.connect(self.loadFigureSalesLoss)


    def loadFigureSalesWon(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        data = self.saleWonRevenue
        date = [d[0].strftime('%Y-%m-%d') for d in data]
        cost = [float(d[1]) for d in data]

        print(data)
        print("DATE: ", date)
        print("COST: ", cost)
        # 1. Example: Replace this with your actual data
        df = pd.DataFrame({'ds': date, 'y': cost})


        # 2. Create and fit the Prophet model
        model = Prophet(interval_width=0.95).fit(df)

        # 3. Forecast future data
        future = model.make_future_dataframe(periods=3, freq='M')
        forecast = model.predict(future)

        # 4. Create figure and plot manually
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot()

        # 5. Plot predicted values (yhat)
        ax.plot(forecast['ds'], forecast['yhat'], label='Predicted Sales (Y-hat)', color='blue')

        # 6. Plot uncertainty interval
        ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], 
                        color='lightcoral', alpha=0.5, label='Uncertainty Interval')

        # 7. Set labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Sales Revenue ₱')
        ax.set_title('Sales Won Forecast')
        ax.grid(True)

        # 8. Clear old widgets
        for i in reversed(range(self.SalesWonForecast_gridLayout.count())):
            widget = self.SalesWonForecast_gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # 9. Create and add canvas
        canvas = FigureCanvas(fig)
        self.SalesWonForecast_gridLayout.addWidget(canvas)
        canvas.draw()

        # 10. Create and add toolbar
        toolbar = NavigationToolbar(canvas, self)
        self.SalesWonForecast_gridLayout.addWidget(toolbar)

        # 11. Custom legend
        custom_lines = [
            Line2D([0], [0], color='blue', lw=2),
            Line2D([0], [0], color='lightcoral', lw=10)
        ]
        fig.legend(custom_lines, ['Predicted Sales (Y-hat)', 'Uncertainty Interval'], loc='upper left')
        fig.tight_layout()

        # Restore the normal cursor
        QApplication.restoreOverrideCursor()

    def loadFigureSalesLoss(self):
            QApplication.setOverrideCursor(Qt.WaitCursor)
            # 1. Example: Replace this with your actual data
            df = pd.DataFrame({'ds': ['2025-01-01', '2025-02-01', '2025-03-01'], 'y': [1000, 1200, 1300]})
            
            # Convert to datetime
            df['ds'] = pd.to_datetime(df['ds'])

            # 2. Create and fit the Prophet model
            model = Prophet(interval_width=0.95)
            model.fit(df)

            # 3. Forecast future data
            future = model.make_future_dataframe(periods=3, freq='M')
            forecast = model.predict(future)

            # 4. Create figure and plot manually
            fig = Figure(figsize=(6, 4))
            ax = fig.add_subplot()

            # 5. Plot predicted values (yhat)
            ax.plot(forecast['ds'], forecast['yhat'], label='Predicted Sales (Y-hat)', color='blue')

            # 6. Plot uncertainty interval
            ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], 
                            color='lightcoral', alpha=0.5, label='Uncertainty Interval')

            # 7. Set labels and title
            ax.set_xlabel('Date')
            ax.set_ylabel('Sales Revenue ₱')
            ax.set_title('Sales Loss Forecast')
            ax.grid(True)

            # 8. Clear old widgets
            for i in reversed(range(self.SalesLossForecast_gridLayout.count())):
                widget = self.SalesLossForecast_gridLayout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

            # 9. Create and add canvas
            canvas = FigureCanvas(fig)
            self.SalesLossForecast_gridLayout.addWidget(canvas)
            canvas.draw()

            # 10. Create and add toolbar
            toolbar = NavigationToolbar(canvas, self)
            self.SalesLossForecast_gridLayout.addWidget(toolbar)

            # 11. Custom legend
            custom_lines = [
                Line2D([0], [0], color='blue', lw=2),
                Line2D([0], [0], color='lightcoral', lw=10)
            ]
            fig.legend(custom_lines, ['Predicted Sales (Y-hat)', 'Uncertainty Interval'], loc='upper left')
            fig.tight_layout()

            # Restore the normal cursor
            QApplication.restoreOverrideCursor()