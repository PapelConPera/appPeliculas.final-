from flask import (
    Blueprint, Flask, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort 

from appPeliculas.db import get_db

bp = Blueprint('actores', __name__,url_prefix="/actores/")
bpapi = Blueprint('api_actores', __name__,url_prefix="api/actores/")

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """SELECT first_name , last_name 
           FROM actor
           ORDER BY first_name, last_name ASC"""
    ).fetchall()
    return render_template('actores/index.html', actor=actores)

@bp.route('/<int:id>')
def detalle(id):
    actores = get_db().execute(
        """SELECT first_name, last_name 
           FROM actor 
           ORDER BY first_name, last_name ASC;
        """,(id,)
    ).fetchone()
    
    pelis = get_db().execute(
        """SELECT *
        FROM film
        WHERE actor_id = ?
        """,(id,)
    ).fetchone()
    return render_template('actores/detalle.html', actor=actores, pelis = pelis)

#-----------------------------------------json--------------------------------------------------------
@bpapi. route('/')
def index_api():
    db = get_db()
    actores= db.execute(
        """SELECT *
        FROM actor
        ORDER BY first_name, last_name """
    ).fetchall()
    return jsonify(actores=actores)

