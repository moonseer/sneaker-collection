from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin

db = SQLAlchemy()

class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sku = db.Column(db.String(30))
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    size = db.Column(db.Integer)
    image = db.Column(db.String(200))
    condition = db.Column(db.String(20))
    location = db.Column(db.String(50))
    description = db.Column(db.String(500))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sku': self.sku,
            'image': self.image 
        }
