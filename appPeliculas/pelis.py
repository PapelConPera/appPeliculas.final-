from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from appPeliculas.db import get_db

bp = Blueprint('pelis', __name__)
bpapi = Blueprint('api_pelis', __name__, url_prefix='api/pelis/')

@bp.route('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT title AS titulo
        FROM actor 
        ORDER BY Peliculas ASC"""

    ).fetchall()
    return render_template('pelis/index.html', pelis=pelis)


@bp.route('/<int:id>')
def get_pelicula(id):
    pelicula = get_db().execute(
        """SELECT *
        FROM film
        WHERE film_id = ?, 
        (id,)"""
    ).fetchone()

    #modificar=
    actor = get_db().execute(
        """SELECT *
        FROM actor
        WHERE actor_id = ?,
        (id,)"""
    ).fetchone()
    return render_template('pelis/detalle.html', pelicula=pelicula, actor = actor)

@bpapi.route('/')
def index_api():
    db = get_db()
    pelis = db.execute(
        """SELECT title AS Peliculas, first_name AS Nombre, last_name AS Apellidos 
           FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id
           JOIN film f ON fa.film_id = f.film_id
           ORDER BY Peliculas ASC"""

    ).fetchall()
    return jsonify(pelis=pelis)