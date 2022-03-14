from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "It works!"

@app.route('/add', methods=["GET"])
def add():
    num1 = request.args.get("num1", type=int)  
    num2 = request.args.get("num2", type=int)
    return { "answer": num1 + num2 }

@app.route('/sub', methods=["POST"])
def sub():
    num1 = request.form.get("num1", type=int)  
    num2 = request.form.get("num2", type=int)
    return { "answer": num1 - num2 }

@app.route('/mult', methods=["POST"])
def mult():
    num1 = int(request.get_json().get("num1")) 
    num2 = int(request.get_json().get("num2"))
    return { "answer": num1 * num2 }

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

app.run(host="0.0.0.0")



