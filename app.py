from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World! :)</h1>"


@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<fahrenheit>')
def f(fahrenheit):
    return f"{float(fahrenheit) * 9.0 / 5 + 32}"


if __name__ == '__main__':
    app.run()
