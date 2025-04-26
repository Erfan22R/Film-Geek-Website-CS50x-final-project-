from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    genre = request.args.get('genre', '').strip()
    director = request.args.get('director', '').strip()
    actor = request.args.get('actor', '').strip()
    start_year = request.args.get('start_year', '').strip()
    end_year = request.args.get('end_year', '').strip()
    min_rating = request.args.get('min_rating', '').strip()

    query = "SELECT * FROM movies WHERE 1=1"
    params = []

    if genre:
        query += " AND Genre LIKE ?"
        params.append(f"%{genre}%")
    if director:
        query += " AND Director LIKE ?"
        params.append(f"%{director}%")
    if actor:
        query += " AND Actors LIKE ?"
        params.append(f"%{actor}%")
    if start_year:
        query += " AND Year >= ?"
        params.append(start_year)
    if end_year:
        query += " AND Year <= ?"
        params.append(end_year)
    if min_rating:
        query += " AND imdbRating >= ?"
        params.append(min_rating)

    conn = get_db_connection()
    cursor = conn.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    if not results:
        return render_template('NotFound.html')
    return render_template('results.html', results=results)

@app.route('/movie/<imdbID>')
def movie_details(imdbID):
    conn = get_db_connection()
    query = "SELECT * FROM movies WHERE imdbID = ?"
    movie = conn.execute(query, (imdbID,)).fetchone()
    conn.close()

    if not movie:
        return "Movie not found."
    return render_template('details.html', movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
