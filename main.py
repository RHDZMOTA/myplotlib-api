from flask import Flask, request, send_file
import numpy as np


import settings
import util

app = Flask(__name__)
settings.init_app(app)


@app.route('/')
def root():
    return """\
    
    Hey there. This is myplotlib-api.
    """


@app.route('/sum', methods=['GET'])
def sum_list():
    numbers = request.args.get('numbers')
    if not numbers:
        return 'Nothing to do here'
    return str(np.sum([float(str(num)) for num in numbers.split(',')]))


@app.route('/scatter', methods=['GET'])
def scatter():
    x_string = request.args.get('x')
    y_string = request.args.get('y')
    xlabel = request.args.get('xlabel')
    ylabel = request.args.get('ylabel')
    title = request.args.get('title')
    try:
        x_vals, y_vals = util.string_to_list(x_string), util.string_to_list(y_string)
    except Exception as e:
        print str(e)
        return 'Nothing to do here.'
    if len(x_vals) != len(y_vals):
        return 'Nothing to do here.'
    response = util.scatter_plot(x_vals, y_vals, xlabel, ylabel, title)
    return response


@app.route('/barplot', methods=['GET'])
def barplot():
    labels_string = request.args.get('labels')
    values_string = request.args.get('values')
    xlabel = request.args.get('xlabel')
    ylabel = request.args.get('ylabel')
    title = request.args.get('title')
    try:
        labels, values = labels_string.split(','), util.string_to_list(values_string)
    except Exception as e:
        print str(e)
        return 'Nothing to do here.'
    if len(labels) != len(values):
        return 'Nothing to do here.'
    response = util.bar_plot(labels, values, xlabel, ylabel, title)
    return response

"""
@app.route('/histogram', methods=['GET'])
def histplot():
    x_string = request.args.get('x')
    bins = request.args.get('bins')
    xlabel = request.args.get('xlabel')
    ylabel = request.args.get('ylabel')
    title = request.args.get('title')
    try:
        x_values = util.string_to_list(x_string)
    except Exception as e:
        print str(e)
        return 'Nothing to do here.'
    response = util.hist_plot(
        x=x_values,
        bins=20 if bins is None else np.int(bins),
        xlabel=xlabel,
        title=title)
    return response
"""


@app.route('/function', methods=['GET'])
def plot_function():
    x_string = request.args.get('x')
    func = request.args.get('func')
    start = request.args.get('start')
    end = request.args.get('end')
    xlabel = request.args.get('xlabel')
    ylabel = request.args.get('ylabel')
    title = request.args.get('title')
    try:
        x_values = util.string_to_list(x_string)
    except Exception as e:
        x_values = None
    response = util.func_plot(func, start, end, x_values, xlabel, ylabel, title)
    return response


if __name__ == '__main__':
    app.run()
