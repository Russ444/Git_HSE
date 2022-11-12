from flask import Flask

app = Flask(__name__)

def conversion(a):
    c = a / 60
    return c

@app.route("/")
def index():

    return "The is a payment page! Please enter the amount in rubles to convert to USD! \a rubles"%(conversion(10))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

