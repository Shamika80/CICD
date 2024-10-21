from flask import Flask, request, jsonify

app = Flask(__name__)

def sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

@app.route('/sum', methods=['POST'])
def sum_route():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'Missing num1 or num2'}), 400
    result = sum(num1, num2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True) 