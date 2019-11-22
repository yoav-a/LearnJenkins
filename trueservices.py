from flask import Flask, render_template, request, jsonify

# Terminal command to send post request: curl -H "Content-Type: application/json" --data @services.json
# http://localhost:5000/response


def get_true_services(json_list):
    res = []
    for elem in json_list:
        if elem['deploy']:
            res.append(elem['service'])
    return res


app = Flask(__name__)


@app.route('/response', methods=['POST', 'GET'])
def response():
    if request.method == 'POST':
        result = get_true_services(request.get_json())
        return jsonify(result)
    else:
        return 'Error - I can only handle POST requests'


if __name__ == '__main__':
    app.run(debug=True)
