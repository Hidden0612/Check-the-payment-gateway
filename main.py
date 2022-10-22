from flask import abort, Flask, request, redirect, render_template, url_for
from functions import *
# ================== # Information # ================== #
app = Flask(__name__, static_folder="static")

# ================== # Home # ================== #
@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

# ================== #  check the payment gateway # ================== #
@app.route("/payment-gateway/search", methods=["GET"])
def payment_gateway():
    if not request.args["link"]: return render_template("unknown.html")
    stat = check_payment_getway(request.args["link"])
    context = {
        "stat":stat,
        "link":request.args["link"]
    }
    return render_template("payment-gateway.html",**context)

@app.route("/payment-gateway", methods=['GET'])
def payment_gateway_search():
    return render_template("payment-gateway-search.html")

# ================== #  credit card search # ================== #
@app.route("/credit-card/search", methods=["GET"])
def credit_card():
    if not request.args["card"] :return render_template("unknown.html")
    print(check_credit_card(request.args["card"]))
    if not check_credit_card(request.args["card"]) :return render_template("unknown.html")
    __card = request.args["card"]
    context = banks.get(str(__card[0:6]))
    if not context:
        return render_template("unknown.html")

    context["number"] = " ".join(j for j in [__card[idx : idx + 4] for idx in range(0, len(__card), 4)])
    return render_template("credit-card.html",**context)

@app.route("/credit-card", methods=['GET'])
def credit_card_search():
    return render_template("credit-card-search.html")

# ================== #  national code # ================== #

@app.route("/national-code/search", methods=["GET"])
def national_code():
    if not request.args["code"]: return render_template("unknown.html")
    stat = check_national_code(request.args["code"])
    context = {
        "stat":stat,
        "code":request.args["code"]
    }
    return render_template("national-code.html",**context)

@app.route("/national-code", methods=['GET'])
def national_code_search():
    return render_template("national-code-search.html")

# ================== # Error 404 # ================== #


# @app.errorhandler(404)
# def error404(error):
#     return "Page Not Found ..."


# ================== # Run # ================== #
if __name__ == "__main__":
    app.run(debug=True)