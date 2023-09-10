
# === Связи МНОГИЕ-КО-МНОГИМ имеет юзер несколько фильмов, как и фильмы несколько юзеров ===
favorite_movie = db.Table(
    'favorite_movie',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)
class FavoriteMovie(db.Model):
    __tablename__ = 'favorite_movie'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    user = db.relationship("User")
    movie = db.relationship("Movie")
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    role = db.Column(db.String(25), nullable=False)
    # Для получения доступа к связанным объектам если не создаем таблицу в виде класса
    favorite_movie = db.relationship("Movie", secondary=favorite_movie, backref="fav_movie")

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)
        # return f"<User {self.name}, {self.favorite_genre_id}>"
