from flask import Flask, jsonify
from flask_cors import CORS
from api.products import apiProducts
from api.admins import apiAdmins
from ecommerce import create_app 
from initialize_db import createDB
from api.categories import apiCategories
from  api.users import apiUsers



app=create_app()
CORS(app) #özellikle bir frontend uygulamasının farklı bir alan adında çalışan bir backend API'sine istek yapması gerektiğinde kullanışlıdır
if __name__ == "__main__":
    createDB()
#app = Flask(__name__)  # flask uygulamasının nesnesini oluşturur
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmins)
app.register_blueprint(apiCategories) # daha düzenli hale getirir.modüllere ayırmayı sağlar 
app.register_blueprint(apiUsers)
@app.route("/")
def index():
    return jsonify({"success": "True", "message": "Main Page"})

@app.route("/shares")  # gideceğim sayfayı belirler
def shares():
    return jsonify({"success": "False", "message": "Not Found"})  # python veri yapılarını JSON verisine dönüştürür (jsonify)

@app.route("/profile")
def profile():
    return {"id": 2, "name": "can", "yas": 21}

if __name__ == "__main__":
    app.run(debug=True)  # debug = true komutu hata ayıklama modunu çalıştırır



# Endpoint genellikle bir API (Application Programming Interface) tarafından sunulan bir hizmetin erişim noktasını ifade eder. 
# Örneğin, bir web API'si kullanarak kullanıcı bilgilerini almak istiyorsanız, bu API'nin "kullanıcılar" gibi bir endpoint'i olabilir.