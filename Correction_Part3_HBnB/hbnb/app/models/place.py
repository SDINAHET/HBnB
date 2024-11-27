from app.models.base_entity import BaseEntity
from app import db

class Place(BaseEntity):
    """
    Model representing a Place entity.
    """
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relationships
    owner = db.relationship('User', back_populates='places')
    reviews = db.relationship('Review', back_populates='place', cascade="all, delete-orphan")
    amenities = db.relationship(
        'Amenity',
        secondary='place_amenity',
        back_populates='places'
    )

    def to_dict(self):
        """
        Converts the Place instance to a dictionary representation.
        """
        base_dict = super().to_dict()
        base_dict.update({
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id
        })
        return base_dict
