import json

from flask import Flask
from flask import abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from cachetools import cached, TTLCache


from config import Config
from api.dbUtils import DbUtils

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)


@app.route("/")
def service():
    return "Service is running!"



@app.route('/addreview', methods=['PUT'])
def addreview():
    if not request.json:
        abort(400)

    reviewData = json.dumps(request.json)
    reviewObject = json.loads(reviewData, object_hook=JSONObject)
    dbUtils = DbUtils()
    dbUtils.add_new_review(reviewObject.product_id, reviewObject.title, reviewObject.review)
    return json.dumps(reviewData)


@app.route('/getproducts', methods=['GET'])
def get_products():
    print('get all')
    products = []
    dbUtils = DbUtils()
    product_data = dbUtils.get_products()
    for r in product_data:
        a = {"title": r[0], "asin": r[1]}
        products.append(a)

    return jsonify(products)


@cached(cache=TTLCache(maxsize=1024, ttl=600))
@app.route('/getproduct/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print(product_id)
    product = []
    dbUtils = DbUtils()
    product_data = dbUtils.get_product_data_by_id(product_id)
    reviews_data =  dbUtils.get_reviews_data_by_id(product_id)
    for r in reviews_data:
        for c in product_data:
            d = {"asin": c[0], "title": c[1]}
            product.append(d)
        a = dict(r)
        product.append(a)


    return jsonify(product)

if __name__ == "__main__":
    app.run()

