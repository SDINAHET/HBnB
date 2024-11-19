#!/usr/bin/python3

# doc à faire partout....


from datetime import datetime
import uuid

class BaseEntity:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Génère un ID UUID4 unique
        self.createdAt = datetime.now()  # Enregistre la date de création
        self.updatedAt = datetime.now()  # Initialise la date de mise à jour

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def update_timestamp(self):
        self.updatedAt = datetime.now()

class User(BaseEntity):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.isAdmin = is_admin

    def registerProfile(self):
        # Code pour enregistrer un profil utilisateur
        pass

    def updateProfile(self, first_name=None, last_name=None, email=None, password=None):
        if first_name:
            self.firstName = first_name
        if last_name:
            self.lastName = last_name
        if email:
            self.email = email
        if password:
            self.password = password
        self.update_timestamp()  # Met à jour la date de modification

    def deleteProfile(self):
        # Code pour supprimer un profil utilisateur
        pass

class Place(BaseEntity):
    def __init__(self, title, description, price, latitude, longitude, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = amenities if amenities else []

    def createPlace(self):
        # Code pour créer un lieu
        pass

    def updatePlace(self, title=None, description=None, price=None, latitude=None, longitude=None, amenities=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if price:
            self.price = price
        if latitude:
            self.latitude = latitude
        if longitude:
            self.longitude = longitude
        if amenities is not None:
            self.amenities = amenities
        self.update_timestamp()  # Met à jour la date de modification

    def deletePlace(self):
        # Code pour supprimer un lieu
        pass

    def listPlaces(self):
        # Code pour lister tous les lieux
        return [self]

class Review(BaseEntity):
    def __init__(self, rating, comment):
        super().__init__()
        self.rating = rating
        self.comment = comment

    def createReview(self):
        # Code pour créer un avis
        pass

    def updateReview(self, rating=None, comment=None):
        if rating is not None:
            self.rating = rating
        if comment:
            self.comment = comment
        self.update_timestamp()  # Met à jour la date de modification

    def deleteReview(self):
        # Code pour supprimer un avis
        pass

    def listReviewsByPlace(self, place):
        # Code pour lister les avis d'un lieu spécifique
        return [self]

class Amenity(BaseEntity):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def createAmenity(self):
        # Code pour créer une commodité
        pass

    def updateAmenity(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        self.update_timestamp()  # Met à jour la date de modification

    def deleteAmenity(self):
        # Code pour supprimer une commodité
        pass

    def listAmenities(self):
        # Code pour lister toutes les commodités
        return [self]
