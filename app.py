from flask import Flask, jsonify
from flask_cors import CORS
from api.products import apiProducts
from api.admins import apiAdmins
from ecommerce import createApp
from ecommerce.initialize_db import createDB 


app=createApp()
CORS(app)
createDB()

app = Flask(__name__)  # flask uygulamasının nesnesini oluşturur
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmins)# daha düzenli hale getirir.modüllere ayırmayı sağlar 

@app.route("/")
def hello_world():
    return jsonify({"success": "True", "message": "Hello World"})

@app.route("/shares")  # gideceğim sayfayı belirler
def shares():
    return jsonify({"success": "False", "message": "Not Found"})  # python veri yapılarını JSON verisine dönüştürür (jsonify)

@app.route("/profile")
def profile():
    return {"id": 1, "name": "can", "yas": 21}

if __name__ == "__main__":
    app.run(debug=True)  # debug = true komutu hata ayıklama modunu çalıştırır
