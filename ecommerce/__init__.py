from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:can34012@localhost:5432/ecommerce  '
   

    db.init_app(app)

    return app

# __init__.py dosyası, bir Python paketinin (module) yapılandırılmasını ve başlatılmasını sağlayan özel bir dosyadır.






