from flask import request, jsonify
from setup import app, db
from models import Movie, Genre, Director, Comment
from schemas import movie_schema, genre_schema, director_schema, comment_schema

@app.route('/genre', methods=['GET', 'POST'])
def add_genre():
    if request.method == 'POST':
        name = request.json['name']
        description = request.json['description']
        new_genre = Genre(name=name, description=description)
        db.session.add(new_genre)
        db.session.commit()
        return genre_schema.jsonify(new_genre)
    
    all_genres = Genre.query.all()
    result = genre_schema.dump(all_genres, many=True)
    return jsonify(result)


@app.route('/director', methods=['GET', 'POST'])
def add_director():
    if request.method == 'POST':
        name = request.json['name']
        biography = request.json['biography']
        new_director = Director(name=name, biography=biography)
        db.session.add(new_director)
        db.session.commit()
        return director_schema.jsonify(new_director)
    
    all_directors = Director.query.all()
    result = director_schema.dump(all_directors, many=True)
    return jsonify(result)

@app.route('/comment', methods=['GET', 'POST'])
def add_comment():
    if request.method == 'POST':
        text = request.json['text']
        movie_id = request.json['movie_id']
        new_comment = Comment(text=text, movie_id=movie_id)
        db.session.add(new_comment)
        db.session.commit()
        return comment_schema.jsonify(new_comment)
    
    all_comments = Comment.query.all()
    result = comment_schema.dump(all_comments, many=True)
    return jsonify(result)

@app.route('/comment', methods=['DELETE'])
def delete_all_comments():
    movie = Movie.query.get(1)
    movie.comments.clear()
    
    db.session.commit()
    return 'Comment were deleted'

@app.route('/movie', methods=['GET','POST'])
def add_movie():
    if request.method == 'POST':
        cover = request.json['cover']
        title = request.json['title']
        description = request.json['description']
        rating = request.json['rating']
        genre_name = request.json['genre_name']
        budget = request.json['budget']
        director_name = request.json['director_name']
        cast = request.json['cast']
        year = request.json['year']
        country = request.json['country']
        language = request.json['language']

        new_movie = Movie(cover=cover, title=title, description=description, rating=rating, budget=budget,
        director_name=director_name, genre_name=genre_name, year=year, country=country, language=language, cast=cast)
        db.session.add(new_movie)
        db.session.commit()
        return movie_schema.jsonify(new_movie)
    
    all_movies = Movie.query.all()
    result = movie_schema.dump(all_movies, many=True)
    return jsonify(result)


@app.route('/movie/<id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    return movie_schema.jsonify(movie)

@app.route('/movie/popular', methods=['GET'])
def get_popular_movies():
    popular_movies = Movie.query.filter(Movie.rating >= 8.0)
    result = movie_schema.dump(popular_movies, many=True)
    return jsonify(result)



@app.route('/director/<name>', methods=['GET'])
def get_director(name):
    director = Director.query.filter_by(name=name).first()
    return director_schema.jsonify(director)

@app.route('/genre/<name>', methods=['GET'])
def get_genre(name):
    movies_by_genre = Movie.query.filter(Movie.genre_name==name)
    result = movie_schema.dump(movies_by_genre, many=True)
    return jsonify(result)

@app.route('/movie/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return f'Movie with id {id} has been deleted'

@app.route('/genre/<id>', methods=['DELETE'])
def delete_genre(id):
    genre = Genre.query.get(id)
    db.session.delete(genre)
    db.session.commit()
    return f'Genre with id {id} has been deleted'