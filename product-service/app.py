from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000
     },
     {
        "id": 2,
        "name": "Keyboard",
        "price": 1500
     },
     {
        "id": 3,
        "name": "Mouse",
        "price": 800
     }
 ]


@app.route("/")
def home():
    return "Product Service is running"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "product-service"
    })


@app.route("/products")
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
