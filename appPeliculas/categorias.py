from flask import (
    Blueprint, flask, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort 

from appPeliculas.db import get_db

bp = Blueprint('categorias', __name__url__prelix="/categorias/")
bpapi = Blueprint('api_categorias', __name__url__prelix="api/categorias/")

@bp. route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT c.name AS categoria, title AS Pelicula
        FROM category c JOIN film_category fc ON c.category_id = fc.categoria
        JOIN film f ON fc.film_id = f.film_id
        ORDER BY Pelicula ASC"""
    ).fetchall()
    return render_template('categoria/index.html', categorias=categorias)




@bp.route('/<int:id>/')
def get_categoria(id):
    categoria = get_db().execute(
        """SELECT *
        FROM film_category
        JOIN category
        WHERE category_id = ?,
        (id,)"""
    ).fetchone()
    return categoria


@bpapi. route('/')
def index_api():
    db = get_db()
    categorias = db.execute(
        """SELECT c.name AS categoria, title AS Pelicula
        FROM category c JOIN film_category fc ON c.category_id = fc.categoria
        JOIN film f ON fc.film_id = f.film_id
        ORDER BY Pelicula ASC"""
    ).fetchall()
    return jsonify(categorias=categorias)