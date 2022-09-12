#!C:/Users/rahul/AppData/Local/Programs/Python/Python310/python.exe
print("Content_Type: text/html\n")

from flask import Flask,render_template, request, redirect,url_for
from DB_Operations import add_text, search_mobile,dbrun,search_serial,search_date

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('add.html')

@app.route("/add_text", methods=["POST", "GET"])
def AddText():
	if request.method == "POST":
		name=request.form["name"]
		mobile=request.form["mobile"]
		address=request.form["address"]
		item=request.form["item"]
		serial=request.form["serial"]
		detail=request.form["detail"]
		service=request.form["service"]
		date=request.form["date"]
		amount=request.form["amount"]
		add_new = add_text(name,mobile,address,item,serial,detail,service,date,amount)
		return redirect(url_for('home'))
	else:
		return render_template('add.html')

@app.route('/search')
def search():
	return render_template('search.html')


@app.route("/search_mobile", methods=["POST", "GET"])
def SearchMobile():
	sum=0
	if request.method == "POST":
		mobile=request.form["mobile"]
		d=search_mobile(mobile)
		for i in d:
			sum=sum+i[9]
		return render_template("result.html", data=d,sum=sum)
	else:
		return render_template("search.html")


@app.route("/search_serial", methods=["POST", "GET"])
def SearchSerial():
	sum=0
	if request.method == "POST":
		serial=request.form["serial"]
		d=search_serial(serial)
		for i in d:
			sum=sum+i[9]
		return render_template("result.html", data=d, sum=sum)
	else:
		return render_template("search.html")

@app.route("/search_date", methods=["POST", "GET"])
def SearchDate():
	sum=0
	if request.method == "POST":
		mobile=request.form["mobile"]
		sdate=request.form["sdate"]
		edate=request.form["edate"]
		d=search_date(mobile,sdate,edate)
		for i in d:
			sum=sum+i[9]
		return render_template("result.html", data=d, sum=0)
	else:
		return render_template("Date_Search.html")

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/date')
def date():
	return render_template('Date_Search.html')


@app.route('/db')
def dbinit():
	d=dbrun()
	return render_template('dbsuccess.html')


	
		
if __name__ == "__main__":
    app.run()