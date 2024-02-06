from barcode import Code128
from barcode.writer import ImageWriter
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/create_tag', methods=['POST'])
def create_tag():
    data = request.get_json()
    product_code = data['product_code']

    barcode = Code128(product_code, writer=ImageWriter())
    filename = f'./tag_codes/barcode_{product_code}'
    barcode.save(filename)

    return jsonify({'filename': filename})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)
