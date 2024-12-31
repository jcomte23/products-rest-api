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
    
    
@app.route("/products/<int:id>")
def getProductById(id):
    product_found = [product for product in products if product["id"] == id]
    
    if len(product_found) > 0:
        return jsonify({
            "status":"success",
            "message": "Request processed successfully",
            "total_records": len(product_found),
            "data": product_found
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": f"Product with ID {id} not found",
            "data": []
        }), 404
        
@app.route("/products/<string:keyword>")
def searchProductByName(keyword):
    products_found = [product for product in products if product["name"] == keyword]
    
    if len(products_found) > 0:
        return jsonify({
            "status":"success",
            "message": "Request processed successfully",
            "total_records": len(products_found),
            "data": products_found
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": f"Product with name '{keyword}' not found",
            "data": []
        }), 404 
                
if __name__ == "__main__":
    app.run(debug=True)