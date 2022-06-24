#!/bin/env python
from app import create_app, socketio
from flask import render_template

app = create_app(debug=True)

# 仮置き、デバッグ用
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=6002)