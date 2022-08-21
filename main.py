import json
from flask import request
from config import app
from models import Order, User, Offer
from service import init_db, get_all, get_by_id, insert_data_user, update_universal, delete_universal, \
    insert_data_order, insert_data_offer


# все пользователи
@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print("Непонятный тип данных")
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


# один пользователь
@app.route("/users/<int:user_id>/", methods=['GET', 'PUT', 'DELETE'])
def get_users_by_id(user_id):
    if request.method == 'GET':
        data = get_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


# все заказы
@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print("Непонятный тип данных")
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


# один заказ
@app.route("/orders/<int:order_id>/", methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_id(order_id):
    if request.method == 'GET':
        data = get_by_id(Order, order_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Order, order_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


# все предложения
@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print("Непонятный тип данных")
    return app.response_class(
        response=json.dumps(request.json, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


# одно предложение
@app.route("/offers/<int:offers_id>/", methods=['GET', 'PUT', 'DELETE'])
def get_offers_by_id(offers_id):
    if request.method == 'GET':
        data = get_by_id(Offer, offers_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(Offer, offers_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Offer, offers_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
