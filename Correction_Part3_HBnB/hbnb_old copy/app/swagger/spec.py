from flask import Blueprint
from flask_restx import Api

# Initialiser Blueprint et l'API Swagger
swagger_bp = Blueprint('swagger', __name__, url_prefix='/swagger')
api = Api(
    swagger_bp,
    version='1.0',
    title='HBnB API',
    description='Documentation interactive pour l\'API HBnB',
    doc='/doc'  # L'URL pour accéder à Swagger UI : /swagger/doc
)

# Importer les namespaces depuis les routes de l'API
from hbnb.app.api.v1.routes.users import ns as users_ns
from hbnb.app.api.v1.routes.places import ns as places_ns
from hbnb.app.api.v1.routes.reviews import ns as reviews_ns
from hbnb.app.api.v1.routes.amenities import ns as amenities_ns

# Ajouter les namespaces à Swagger
api.add_namespace(users_ns, path='/api/v1/users')
api.add_namespace(places_ns, path='/api/v1/places')
api.add_namespace(reviews_ns, path='/api/v1/reviews')
api.add_namespace(amenities_ns, path='/api/v1/amenities')
