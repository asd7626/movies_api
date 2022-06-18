from setup import ma
from models import Movie, Genre, Director, Comment

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        include_fk = True
    
    comments = ma.auto_field()
        
class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        include_fk = True
    
    movies = ma.auto_field()
    
class DirectorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Director
        include_fk = True
    
    movies = ma.auto_field()

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        include_fk = True
    

movie_schema = MovieSchema()
genre_schema = GenreSchema()
director_schema = DirectorSchema()
comment_schema = CommentSchema() 