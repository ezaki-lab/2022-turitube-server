#!/bin/env python
from app import create_app, socketio
from flask import render_template, send_from_directory
import os

app = create_app(debug=True)

static_path = os.path.dirname(__file__) + "/static/" #

# 仮置き、デバッグ用
@app.route('/img/<directory>/<path>')
def send_img(directory, path):
    print(os.path.dirname(__file__))
    print(static_path, directory, path)
    return send_from_directory(f"{static_path}img/{directory}/", path, as_attachment=False)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=6002)