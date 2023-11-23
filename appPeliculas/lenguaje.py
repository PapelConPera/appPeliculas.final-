from flask import (
    Blueprint, Flask, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort 

from appPeliculas.db import get_db

bp = Blueprint('lenguajes', __name__,url_prefix="/lenguaje/")
bpapi = Blueprint('api_lenguajes', __name__,url_prefix="api/lenguaje/")

@bp. route('/')
def index():
    db = get_db()
    lenguaje = db.execute(
        """SELECT c.name AS lenguaje, f.title AS titulo, release_year AS año
        FROM lenguage l JOIN film f ON l.lenguage_id = f.lenguge_id
        ORDER BY name ASC"""
    ).fetchall()
    return render_template('lenguaje/index.html', lenguaje=lenguaje)


@bp.route('/<int:id>')
def detalle(id):
    lenguaje = get_db().execute(
        """SELECT *
        FROM languaje
        WHERE languaje_id = ?,
        (id,)"""
    ).fetchone()
    return render_template('lenguje/detalle.html', lenguaje=lenguaje)


@bpapi.route('/')
def index_api():
    db = get_db()
    lenguaje = db.execute(
        """SELECT c.name AS lenguaje, f.title AS titulo, release_year AS año
        FROM lenguage l JOIN film f ON l.lenguage_id = f.lenguge_id
        ORDER BY name ASC"""
    ).fetchall()
    return jsonify(lenguajes=lenguaje)