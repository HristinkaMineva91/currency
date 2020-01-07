import os
import requests 

from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import src.currency

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")
    response = requests.get("http://data.fixer.io/api/latest", params={"access_key":"0da5c0ba1a0ffeeb7385f8ece1818fa7", "base": "EUR", "symbols": currency})
    if response.status_code != 200:
        return jsonify({"success": False})

    data = response.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})