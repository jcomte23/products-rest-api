from flask import Flask, jsonify
from database import products

app = Flask(__name__)

@app.route("/products")
def getProducts():
    return jsonify({
        "status":"success",
        "message": "Request processed successfully",
        "total_records": len(products),
        "data": products
    }), 200

if __name__ == "__main__":
    app.run(debug=True)