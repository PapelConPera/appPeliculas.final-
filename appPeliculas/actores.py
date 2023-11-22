from flask import (
    Blueprint, flask, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort 

from movies.db import get_db

bp = Blueprint('actores', __name__url__prelix="/actor/")
bpapi = Blueprint('actores', __name__url__prelix="api/actor/")

@bp. route('/')
def index():
    db = get_db()
    actores= db.execute(
        """SELECT *
        FROM actor
        ORDER BY first_name, last_name """
    ).fetchall()
    return render_template('actores/index.html', actores=actores)

@bp.route('/create', methods=(['GET']))

def get_actor(id):
    actor = get_db().execute(
        """SELECT *
        FROM actor
        WHERE actor_id = ?,
        (id,)"""
    ).fetchone()
    return actor


@bpapi. route('/')
def index_api():
    db = get_db()
    actores= db.execute(
        """SELECT *
        FROM actor
        ORDER BY first_name, last_name """
    ).fetchall()
    return jsonify(actores=actores)

