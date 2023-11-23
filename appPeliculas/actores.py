from flask import (
    Blueprint, Flask, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort 

from appPeliculas.db import get_db

bp = Blueprint('actores', __name__,url_prefix="/actor/")
bpapi = Blueprint('api_actores', __name__,url_prefix="api/actor/")

@bp. route('/')
def index():
    db = get_db()
    actores= db.execute(
        """SELECT *
        FROM actor
        ORDER BY first_name, last_name """
    ).fetchall()
    return render_template('actores/index.html', actores=actores)

@bp.route('/<int:id>')
def get_actor(id):
    actor = get_db().execute(
        """SELECT *
        FROM actor
        WHERE actor_id = ?,
        (id,)"""
    ).fetchone()
    
    #modificar=
    pelis = get_db().execute(
        """SELECT *
        FROM pelis
        WHERE actor_id = ?,
        (id,)"""
    ).fetchone()
    return render_template('actores/detalle.html', actor=actor, pelis = pelis)


@bpapi. route('/')
def index_api():
    db = get_db()
    actores= db.execute(
        """SELECT *
        FROM actor
        ORDER BY first_name, last_name """
    ).fetchall()
    return jsonify(actores=actores)

