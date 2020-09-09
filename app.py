from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'this is my test page with flask <h1>testing page 1</h1> '

if __name__ == '__main__':
    app.run(debug=True)    