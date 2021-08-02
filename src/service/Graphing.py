from matplotlib import pyplot as plt
from matplotlib.figure import Figure 
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# createSimpleGraph returns a graph given
# int[] x and int[] y
def createSimpleGraph(x, y, coin, time):
	fig = Figure()
	fig.set_size_inches(8, 5)
	axis = fig.add_subplot(1,1,1)
	title = "Price of " + str(coin) + " in the past " + str(time) + " hours."	
	axis.set_title(title)
	axis.yaxis.set_major_formatter('${x:1.2f}')
	axis.yaxis.set_tick_params(which='major', labelcolor='green')
	axis.autoscale(tight=True)
	axis.plot(x, y)
	canvas = FigureCanvas(fig)
	output = BytesIO()
	canvas.print_png(output)
	return output.getvalue()








