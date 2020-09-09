from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'this is my test page with flask '

if __name__ == '__main__':
    app.run(debug=True)    