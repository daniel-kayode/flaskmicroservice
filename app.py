from flask import Flask, jsonify

app = Flask(__name__)

def change(amount):
    res = []
    coins = [25, 10, 5, 1]  # value of quarters, dimes, nickels, pennies
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # convert amount to cents
    amount = int(amount * 100)

    for coin in coins:
        num, amount = divmod(amount, coin)
        if num > 0:
            res.append({coin_lookup[coin]: num})
    
    return res

@app.route('/')
def hello():
    return 'Hello World! I can make change at route: /change/<dollar>/<cents>'

@app.route('/change', defaults={'dollar': None, 'cents': None})
@app.route('/change/<int:dollar>', defaults={'cents': 0})
@app.route('/change/<int:dollar>/<int:cents>')
def changeroute(dollar, cents):
    if dollar is None or cents is None:
        return jsonify(error="You must provide both dollar and cents values."), 400
    
    amount = dollar + cents / 100.0
    result = change(amount)
    return jsonify(result)

@app.route('/100/change/<int:dollar>/<int:cents>')
def change100route(dollar, cents):
    amount = dollar + cents / 100.0
    amount100 = amount * 100
    result = change(amount100 / 100.0)  # amount100 should be divided by 100.0 to get the correct amount
    return jsonify(result)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
