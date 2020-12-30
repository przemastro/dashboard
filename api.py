from flask import Flask, render_template, request, redirect
from mongoDBConnector import getValues
from plots import diggingPieChart, testCenterComponentsPieChart, treesPieChart, cyclingBarChart, linePlot, weightChart

app = Flask(__name__)
address = "localhost"

@app.route("/")
def getData():
    count = getValues()
    diggingPieChart()
    testCenterComponentsPieChart()
    treesPieChart()
    cyclingBarChart()
    linePlot()
    weightChart()
    return render_template("index.html", count=count)


# Handling COR requests
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,SessionId,Email')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add("Access-Control-Max-Age", "3600");
    response.headers.add("Access-Control-Allow-Headers", "x-requested-with");
    response.headers.add("Connection", "keep-alive");
    response.headers.add("Vary", "Accept-Encoding");
    return response

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False, host=address, port=5000, threaded=True, use_reloader=True)
