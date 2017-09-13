import matplotlib.pyplot as plt
import numpy as np
import StringIO

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import sin, cos, tan, arcsin, arccos, arctan, e, pi, log, exp
ln = log


def indicator(statement):
    return 1 if statement else 0


def factorial(x):
    return 1 if x < 1 else x * factorial(x - 1)


def step(x, a, b):
    return 1 if (x < b) and (a < x) else 0


def string_to_list(string):
    return [np.float(element) for element in string.split(',')]


def scatter_plot(x, y, xlabel=None, ylabel=None, title=None):
    # Create empty figure
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    # Plot data
    ax.plot(x, y, '.')
    plt.title(title if title else 'Scatterplot')
    plt.xlabel(xlabel if xlabel else 'x-values')
    plt.ylabel(ylabel if ylabel else 'y-label')
    # Create canvas
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    return output.getvalue()


def bar_plot(labels, values, xlabel=None, ylabel=None, title=None):
    # Create empty figure
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    # Plot data
    label_position = np.arange(len(labels))
    ax.bar(label_position, values, color="blue", align='center', alpha=0.75)
    plt.xticks(label_position, labels)
    plt.title(title if title else 'Barplot')
    plt.xlabel(xlabel if xlabel else 'x-values')
    plt.ylabel(ylabel if ylabel else 'y-label')
    # Create canvas
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    return output.getvalue()


def hist_plot(x, bins, xlabel=None, title=None):
    def histogram(elements, intervals, func):
        return [func(list(filter(lambda x: (x >= a) and (x < b), elements))) for a, b in intervals]
    min_val, max_val = min(x), max(x)
    step = (max_val - min_val) / bins
    step = step * 1.05
    lower_limits = np.arange(min_val, max_val + step, step)
    intervals = list(zip(lower_limits[:-1], lower_limits[1:]))
    hist_vals = histogram(x, intervals, len)
    return bar_plot(intervals, hist_vals, xlabel, 'Frequency (Count)', title if title else 'Histogram')


def func_plot(funcs, start=None, end=None, x=None, xlabel=None, ylabel=None, title=None):

    def replace_string(target, patterns):
        return target if not len(patterns) else replace_string(
            target.replace(patterns[0], ""), patterns[1:])

    def allowed_function(string_func):
        key_words = ["sin", "cos", "tan", "arcsin", "arccos",
                     "arctan", "e", "pi", "log", "ln", "exp",
                     "x", "**", "*", "+", "-", "/", "(", ")",
                     " ", "", "indicator", "factorial", "step",
                     "<", ">", "<=", ">=", "==", "!="]
        try:
            just_numbers = replace_string(string_func, key_words)
            if not len(just_numbers):
                return True
            float(just_numbers)
            return True
        except Exception as e:
            # print str(e)
            return False

    def complete_info():
        if (start is None) or (end is None):
            if x is None:
                return False
            return True
        return True

    if not complete_info():
        return "Not complete info."

    funcs = funcs.replace('^', '**')
    start = eval(start) if allowed_function(start) else 0.01
    end = eval(end) if allowed_function(end) else 20
    x = x if x is not None else np.arange(start, end + (end - start) / 10000.0, (end - start) / 10000.0)

    list_functions = funcs.split(',')
    if np.sum([allowed_function(string_func) for string_func in list_functions]) != len(list_functions):
        return """No."""

    legends = list_functions
    f_list = [eval('lambda x: ' + func) for func in list_functions]
    ys = [[f(element) for element in x] for f in f_list]
    # Create empty figure
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    # Plot data
    for y, label in zip(ys, legends):
        ax.plot(x, y, label=label)
    plt.title(title if title else 'Plot')
    plt.xlabel(xlabel if xlabel else 'x-values')
    plt.ylabel(ylabel if ylabel else 'y-values')
    plt.legend()
    # Create canvas
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    return output.getvalue()
