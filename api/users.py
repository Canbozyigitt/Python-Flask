from flask import Flask ,jsonify ,Blueprint, request
from ecommerce.models import User

apiUsers=Blueprint('apiUsers', __name__, url_prefix='/api/users')

@apiUsers.route('/')

def users():
    try:
        allUsers=Use.get_all_users()
        users=[]

        for user in allUsers:
            users.append({"id": user.id,"username":user.username,"email":user.email,"password":user.password})
    
        return jsonify({"success":True,"data":users,"count":len(users)})
    except Exception as e:
        return jsonify({"success":False,"message":"There is an error !"})

@apiUsers.route("/<int:id>")
def user(id):
    try:
        user=User.get_user_by_id(id)
        userObj={"id":user.id,"username":user.username,"email":user.email,"password":user.password}
        return jsonify({"success":True,"data":userObj})
    except Exception as e:
         return jsonify({"success":False,"message":"There is an error !"})
    

@apiUsers.route("/addUser",form=["GET","POST","PUT","DELETE"])
# put: veriyi güncellemek için kullanılır
# put, post , get vb komutlar http  istek komutlarıdır (request bunları temsil eder) 
# yani bu komutlara request methoları sayesinde erişebilrisin 
def addUser(): 
    try:
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        User.add_user(username,email,password)
        return jsonify({"success":True,"message":"User added successfully"})
    except Exception as e:
        return jsonify({"success":False,"message":"There is an error"})