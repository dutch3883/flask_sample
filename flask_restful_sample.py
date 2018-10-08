from flask_restful import Api,Resource
from flask import Flask, render_template,request,jsonify

app = Flask(__name__)
api = Api(app)

all_user = [{"username":"user1","fname":"John","lname":"Tester"},
				{"username":"user2","fname":"Mary","lname":"Something"}]
username_set = {"user1","user2"}
				
class User(Resource):
	
	def get(self,username):
		for i in all_user:
			if i["username"] == username:
				print(username)
				return i
			
		
	def post(self):
		new_user = {
			"username" : request.form['username'],
			"fname" : request.form['fname'],
			"lname": request.form['lname']
		}
		if new_user['username'] in username_set:
			return {"status":400,"message":"username is exist"},400
			
		all_user.append(new_user)
		return {"status":200,"message":"Add user success"}
		
		
api.add_resource(User,"/api/users")
api.add_resource(User,"/api/users/<string:username>")

app.run("0.0.0.0","18085")