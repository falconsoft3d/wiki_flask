from flask import Flask, jsonify, request
app = Flask(__name__)


from products import products


@app.route("/ping")
def ping():
    return "pong"

@app.route("/ping2")
def ping2():
    return jsonify({"mensaje":"Hello Word"})

@app.route("/products", methods=["GET"])
def getProducts():
    return jsonify({"products":products, "message": "Product List"})

@app.route("/products/<string:product_name>", methods=["GET"])
def getProduct(product_name):
    produtsFound = [product for product in products if product["name"] == product_name] 
    if (len(produtsFound) > 0):
            return jsonify({"products":produtsFound[0]})
    return jsonify({"message": "Product not found"})


# Adicionando un producto
@app.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "name" : request.json["name"],
        "price" : request.json["price"],
    }
    products.append(new_product)
    return jsonify({"message":"product added succesfully","produts": products })

# Editamos un producto
@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
    produtsFound = [product for product in products if product["name"] == product_name]
    if (len(produtsFound) > 0):
        produtsFound[0]["name"] = request.json["name"]
        produtsFound[0]["price"] = request.json["price"]
        return jsonify({
            "message":"Product Update",
            "produt": produtsFound[0] })

    return jsonify({"message": "Product not found"})


# Borramos un producto
@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteProduct(product_name):
    produtsFound = [product for product in products if product["name"] == product_name]
    if (len(produtsFound) > 0):
        products.remove(produtsFound[0])
        return jsonify({
                "message":"Product Deleted",
                "produts": products })
    return jsonify({"message": "Product not found"})



if __name__ == "__main__":
    app.run(debug=True, port=4000)
