from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about')
def hello():
    return jsonify({'about': 'Hello Pankaj'})

if __name__ == '__main__':
    app.run(debug=True)