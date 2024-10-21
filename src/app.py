import os
from flask import Flask, jsonify, request
from modules.AddOp import add 
from modules.SubOp import sub
from modules.mult import mult

app = Flask(__name__)

def f(x,y):
    if y == 0:
        raise  ValueError("Cannot divide by zero")
    return x/y


operations = {
    'add' : lambda x , y : add(x,y),
    'subtract' : lambda x , y : sub(x,y),
    'multiply' : lambda x , y : mult(x,y),
    'divide' : lambda x , y : f(x,y) ,

}


    

@app.route('/<op>/<op1>/<op2>', methods=['GET'])
def handle_calculation(op, op1=1, op2=2):
    try :
        op1 = int(op1)
        op2 = int(op2)
    except  ValueError:
        return jsonify({"error" : "Invalid input"}), 400
    if op not in operations:
        return jsonify({'status': 400, 'message': f'Invalid operation: {op}'}), 400

    try :
        result = round(operations[op](op1, op2),5)
        return jsonify({'status': 200, 'result': f'{result}'}), 200
    except  ValueError as e:
        return jsonify({'status': 400, 'message': str(e)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 404, 'message': str(request)}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))

    app.run(host='0.0.0.0', port=port)


