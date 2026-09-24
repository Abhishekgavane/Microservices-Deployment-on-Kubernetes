from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {
        "id": 101,
        "product": "Laptop",
        "quantity": 1,
        "status": "CONFIRMED"
     },
     {
                            "id": 102,
                                    "product": "Keyboard",
                                            "quantity": 2,
                                                    "status": "PROCESSING"
     }
 ]


@app.route("/")
def home():
    return "Order Service is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "order-service"
     })


@app.route("/orders")
def get_orders():
    return jsonify(orders)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
