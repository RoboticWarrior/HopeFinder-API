from flask import Flask, jsonify, request
from core.vod import vod
from core.search import search

app = Flask(__name__)


@app.route('/vod')
def vod_route():
    return jsonify({'vod': vod()})


@app.route('/search', methods = ['POST'])
def search_route():
    return jsonify({'results': search(request.get_json()['query'])})


if __name__ == '__main__':
    app.run(debug=True)