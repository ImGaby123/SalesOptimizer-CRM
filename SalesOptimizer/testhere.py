import matplotlib.pyplot as plt

#-- In your case, you'd do something more like:
# from matplotlib.figure import Figure
# fig = Figure()
#-- ...but we want to use it interactive for a quick example, so 
#--    we'll do it this way
fig, axes = plt.subplots(nrows=4, ncols=4)

for i, ax in enumerate(axes.flat, start=1):
    ax.set_title('Test Axes {}'.format(i))
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')

plt.show()