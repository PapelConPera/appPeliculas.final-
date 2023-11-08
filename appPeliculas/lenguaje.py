from flask import (
    Blueprint, flask, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort 

from movies.db import get_db

bp = Blueprint('lenguajes', __name__url__prelix="/lenguaje/")

@bp. route('/')
def index():
    db = get_db()
    lenguaje = db.execute(
        """SELECT c.name AS lenguaje, f.title AS titulo, release_year AS año
        FROM lenguage l JOIN film f ON l.lenguage_id = f.lenguge_id
        ORDER BY name ASC"""
    ).fetchall()
    return render_template('lenguaje/index.html', lenguajes=lenguaje)

@bp.route('/create', methods=(['GET']))

def get_lenguaje(id):
    lenguaje = get_db().execute(
        """SELECT *
        FROM languaje
        WHERE languaje_id = ?,
        (id,)"""
    ).fetchone()