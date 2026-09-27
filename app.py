from flask import Flask, jsonify, request
import os
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
    production = os.environ.get('FLASK_DEBUG', 'false').lower()

    if production == 'true':
        app.run(debug=False)

    elif production == 'false':
        app.run(debug=True)