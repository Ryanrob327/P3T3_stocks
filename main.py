# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from API.stocks import stocks_api
from API.GME import GME_api
from API.TSLA import TSLA_api
from API.GOOGL import GOOGL_api
from API.AAPL import AAPL_api
from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(stocks_api) # register api routes
app.register_blueprint(GME_api) # register api routes
app.register_blueprint(TSLA_api) # register api routes
app.register_blueprint(GOOGL_api) # register api routes
app.register_blueprint(AAPL_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/ProjectPlan/')  
def project_plan():
    return render_template("project_plan.html")
# uncomment this when ready for use
@app.route('/GraphTest/')
def Graph_test():
    return render_template('Graph_test.html')

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
