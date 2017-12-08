from flask import Flask, jsonify, render_template, request
from redis import Redis
from flask import abort
import json

app = Flask(__name__)
myJsonData = json.loads(open('./ElClassico.json').read())

summaryData = myJsonData["summary"]
laligaData = myJsonData["laliga"]
copaData = myJsonData["copa del rey"]

@app.route("/", methods=['GET'])
def get_sum():
	sumList = []
	for element in summaryData:
		sumList.append(element)
	return render_template("summary.html", display_data=sumList)

@app.route("/laliga", methods=['GET'])
def get_laliga():
	laList = []
	for element in laligaData:
		laList.append(element)
	return render_template("laliga.html", display_data=laList)

@app.route("/copa", methods=['GET'])
def get_copa():
	copaList = []
	for element in copaData:
		copaList.append(element)
	return render_template("copa.html", display_data=copaList)

@app.route("/laliga/<int:year>/", methods=['GET'])
def get_laliga_yr(year):
	myyrlist = []
	for element in laligaData:
		if element["Year"] == year:
			myyrlist.append(element)
	return render_template("laliga.html", display_data=myyrlist)

@app.route("/copa/<int:year>/", methods=['GET'])
def get_copa_yr(year):
	myyrlist = []
	for element in copaData:
		if element["Year"] == year:
			myyrlist.append(element)
	return render_template("copa.html", display_data=myyrlist)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)
