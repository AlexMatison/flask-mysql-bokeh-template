from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import db
import chart

from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid,
                          Range1d)
from bokeh.models.glyphs import VBar
from bokeh.plotting import figure
#from bokeh.charts import Bar
from bokeh.embed import components
from bokeh.models.sources import ColumnDataSource


web_blueprint = Blueprint('web', __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')

@web_blueprint.route('/', defaults={'page': 'index'})
@web_blueprint.route('/<page>')
def index(page):
    random_parameter = request.args.get('random_parameter', default = "You didn't use a parameter", type = str)
    try:
        print(page)
        return render_template('pages/%s.html' % page, welcome_msg='Hi there', random_parameter=random_parameter)
    except TemplateNotFound:
        abort(404)


@web_blueprint.route('/plot')
def plot():
    data = db.get_garbage_mysql()
    myplot = chart.generate_plot(data)
    script, div = components(myplot)
    plot_title = 'Line plot'
    return render_template("pages/chart.html", plot_title=plot_title,
                           the_div=div, the_script=script)
