from flask import Flask, json, jsonify, request

# TODO: ACTUAL IMPLEMENTATION

app = Flask(__name__)

f = open('src/data/dummyImageFile.json')
data = json.load(f)

@app.route('/images')
def get_images():
    response = jsonify(data)
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run()