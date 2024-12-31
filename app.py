from flask import Flask, jsonify, request
from database import products

app = Flask(__name__)

@app.route("/products")
def get_products():
    return jsonify({
        "status":"success",
        "message": "Request processed successfully",
        "total_records": len(products),
        "data": products
    }), 200
    
    
@app.route("/products/<int:product_id>")
def get_product_by_id(product_id):
    product_found = [product for product in products if product["id"] == product_id]
    
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
def search_product_by_name(keyword):
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

@app.route("/products", methods=["POST"])
def add_product():
    new_product = request.get_json()

    if "name" not in new_product or "price" not in new_product or "quantity" not in new_product:
        return jsonify({
            "status": "error",
            "message": "Invalid request payload. Expected JSON object with 'name', 'price', and 'quantity' fields."
        }), 400

    for product in products:
        if product["name"] == new_product["name"]:
            return jsonify({
                "status": "error",
                "message": f"Product with name '{new_product['name']}' already exists."
            }), 400

    new_product["id"] = len(products) + 1
    products.append(new_product)

    return jsonify({
        "status": "success",
        "message": "Product added successfully",
        "data": new_product
    }), 201

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    updated_product = request.get_json()

    if "name" not in updated_product or "price" not in updated_product or "quantity" not in updated_product:
        return jsonify({
            "status": "error",
            "message": "Invalid request payload. Expected JSON object with 'name', 'price', and 'quantity' fields."
        }), 400

    product_found = [product for product in products if product["id"] == product_id]

    if len(product_found) == 0:
        return jsonify({
            "status": "error",
            "message": f"Product with ID {product_id} not found."
        }), 404

    product_found[0]["name"] = updated_product["name"]
    product_found[0]["price"] = updated_product["price"]
    product_found[0]["quantity"] = updated_product["quantity"]

    return jsonify({
        "status": "success",
        "message": "Product updated successfully",
        "data": product_found[0]
    }), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product_found = [product for product in products if product["id"] == product_id]

    if len(product_found) == 0:
        return jsonify({
            "status": "error",
            "message": f"Product with ID {product_id} not found."
        }), 404

    products.remove(product_found[0])

    return jsonify({
        "status": "success",
        "message": "Product deleted successfully"
    }), 200
                
if __name__ == "__main__":
    app.run(debug=True)