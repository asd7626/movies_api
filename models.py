from setup import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cover = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    cast = db.Column(db.String(1000), nullable=False)
    genre_name = db.Column(db.String(100), db.ForeignKey('genre.name'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('movies', lazy=True))

    director_name = db.Column(db.String(100), db.ForeignKey('director.name'), nullable=False)
    director = db.relationship('Director', backref=db.backref('movies'), lazy=True)

    
    def __repr__(self):
        return self.title

    

class Comment(db.Model):
    
    text = db.Column(db.String(200), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    movie = db.relationship('Movie', backref=db.backref('comments'), lazy=True)

    def __repr__(self):
        return self.text

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return self.name

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.name