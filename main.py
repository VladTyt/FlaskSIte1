from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/technology')
def technology():
    return render_template('technology.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run(debug=True)