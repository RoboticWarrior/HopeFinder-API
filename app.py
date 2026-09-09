from flask import Flask, jsonify, request
from services.vod import vod
from services.search import search

app = Flask(__name__)


@app.route('/vod')
def vod_route():
    return jsonify({'vod': vod()})


@app.route('/search', methods = ['POST'])
def search_route():
    query = request.get_json()['query']

    return jsonify({'results': search(query)})


if __name__ == '__main__':
    app.run(debug=True)