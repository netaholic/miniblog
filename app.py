from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>This is the index page of the blog being developed with Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)    