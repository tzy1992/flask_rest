from flask import Flask,jsonify,request,Response
import json
from flask import request, render_template, redirect, url_for
import MySQLdb

app = Flask(__name__)


db = MySQLdb.connect("localhost", "root", "", "yii2advanced")


@app.route('/user', methods=['GET'])
def get_user():
	#curs = db.cursor()
	curs = db.cursor(MySQLdb.cursors.DictCursor)
	curs.execute("SELECT username, email, role from user")
	data = curs.fetchall()

	formatted_user = []
	for i in data:
		formatted_user.append([i["username"], i["email"], i["role"]])

	return jsonify(Users = formatted_user)

@app.route('/add', methods=['POST'])
def add_user():
	curs = db.cursor(MySQLdb.cursors.DictCursor)
	req_json = request.get_json()

	curs.execute("INSERT INTO yii2advanced.user (username, email, role) VALUES (%s,%s,%s)", (req_json['username'], req_json['email'], req_json['role']))
	db.commit()
	resp = Response("Updated", status=201, mimetype='application/json')
	return resp

@app.route('/user/<string:username>', methods=['DELETE'])
def delete_user(username):
	curs = db.cursor(MySQLdb.cursors.DictCursor)
	curs.execute("SELECT username, email, role from user")
	data = curs.fetchall()
	user = curs.query.get_or_404(username)
	delete(user)
	resp = Response("Delete", status=201, mimetype='application/json')
	return resp



	

if __name__ == "__main__":
	app.run()


		