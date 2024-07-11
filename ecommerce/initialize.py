#from ecommerce.models import db
#from ecommerce import createApp

#def createDB():
#    db.create_all(app=createApp())
# ecommerce/initialize_db.py

from .models import db
from . import createApp

def createDB():
    app = createApp()
    with app.app_context():
        db.create_all()

    