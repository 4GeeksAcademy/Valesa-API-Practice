from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# usuario

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

    # Aqui va Planeta 

    class Planets(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        url = db.Column(db.String(250), nullable=False)
        diameter = db.Column(db.String(250), nullable=False)
        population = db.Column(db.String(250), nullable=False)
        climate = db.Column(db.String(250), nullable=False)
        terrain = db.Column(db.String(250), nullable=False)
        surfaceWater = db.Column(db.String(250), nullable=False)
        rotationPeriod = db.Column(db.String(250), nullable=False)
        orbitalPeriod = db.Column(db.String(250), nullable=False)
        gravity = db.Column(db.String(250), nullable=False)
        films = db.Column(db.String(250), nullable=False)
        created = db.Column(db.String(250), nullable=False)
        edited = db.Column(db.String(250), nullable=False)
        favorites = db.relationship('Favorites', backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "diameter": self.diameter,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surfaceWater": self.surfaceWater,
            "rotationPeriod": self.rotationPeriod,
            "orbitalPeriod": self.orbitalPeriod,
            "gravity": self.gravity,
            "films": self.films,
            "created": self.created,
            "edited": self.edited,
        }



