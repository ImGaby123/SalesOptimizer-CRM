import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# 1. Data Frame
df = pd.DataFrame({'ds': ['2025-01-01', '2025-02-01', '2025-03-01'], 'y': [1000, 1200, 1300]})

# 2. Create Model and Assign Confidence Interval
model = Prophet(interval_width=0.95).fit(df)  # 95% Confidence Interval

# 3. Prepare Dataframe adding future data
future = model.make_future_dataframe(periods=3, freq='M')

# 4. Call the Predict Method
forecast = model.predict(future)

# 5. Plot the stuff
fig = model.plot(forecast)

# 6. Giving Figure access
ax = fig.gca()


# 7. Change Color and Customize the legend to match the lines and shaded area
for fc in ax.collections:
    # Uncertainty Interval Color
    fc.set_facecolor('lightcoral')

from matplotlib.lines import Line2D
custom_lines = [
    Line2D([0], [0], color='blue', lw=2),          # Forecast line
    Line2D([0], [0], color='lightcoral', lw=10)    # Uncertainty Interval Interval 
]


# 8. Calling plt to show the graphs
plt.legend(custom_lines, ['Predicted Sales (Y-hat)', 'Uncertainty Interval'], loc='upper left')
plt.title('Sales Forecast')
plt.grid(True)
plt.tight_layout()
plt.show()
