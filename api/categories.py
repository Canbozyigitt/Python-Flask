from flask import Flask ,jsonify ,Blueprint

apiCategories=Blueprint('apiCategories', __name__, url_prefix='/api/categories')
@apiCategories.route('/')
def index():
    return jsonify({"success": True, "message": "Hello Categories"})
