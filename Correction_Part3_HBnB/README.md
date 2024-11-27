en cours de correction la version finale corrigé fonctionnant à 100% avec les test unitest et pytest arrive bientôt.................


[![HBnB CI](https://github.com/SDINAHET/HBnB/actions/workflows/test.yml/badge.svg)](https://github.com/SDINAHET/HBnB/actions/workflows/test.yml)





```plaintext
HBnB
|---.github
|   |   |---workflows
|   |       |---test.yml
|---Correction_Part3_HBnB
<!-- |   |---.github
|   |   |---workflows
|   |       |---test.yml -->
|   |---app
|       |---tests
```

```plaintext
HBnB
|---.github
|   |   |---workflows
|   |       |---test.yml
|---Correction_Part3_HBnB
|   |---app
|       |---tests
```

HBnB/
├── Correction_Part3_HBnB/
|   |app
│   |   ├── api/
│   |   │   ├── __init__.py
│   |   │   ├── v1/
│   |   │   │   ├── __init__.py
│   |   │   │   ├── routes/
│   |   │   │   │   ├── auth.py
│   |   │   │   │   ├── users.py
│   |   │   │   │   ├── places.py
│   |   │   │   │   ├── reviews.py
│   |   │   │   │   ├── amenities.py
│   |   ├── instance/
│   |   │   ├── development.db
│   |   │   ├── config.py
│   |   ├── app/
│   |   │   ├── __init__.py
│   |   │   ├── models/
│   |   │   │   ├── base_model.py
│   |   │   │   ├── user.py
│   |   │   │   ├── place.py
│   |   │   │   ├── review.py
│   |   │   │   ├── amenity.py
│   |   │   ├── repository/
│   |   │   │   ├── repository.py
│   |   │   ├── services/
│   |   │   │   ├── facade.py
│   |   │   ├── tests/
│   |   │   ├── routes/
│   |   │   ├── swagger/
    ├── config.py
    ├── run.py
│   ├── requirements.txt
├── .github/
│   ├── workflows/
│   │   ├── test.yml


HBnB/
├── Correction_Part3_HBnB/
|   |──hbnb/
|   |   |── app/
│   |   |   |── api/
│   |   │   |   ├── __init__.py
│   |   │   |   ├── v1/
│   |   │   |   │   ├── __init__.py
|   │   │   |   │   ├── auth.py
|   │   │   |   │   ├── users.py
|   │   │   |   │   ├── places.py
|   │   │   |   │   ├── reviews.py
|   │   │   |   │   ├── amenities.py
|   │   │   |   │   ├── protected.py
│   |   │   ├── __init__.py
│   |   │   ├── models/
│   |   │   |   ├── __init__.py
│   |   │   │   ├── base_entity.py
│   |   │   │   ├── user.py
│   |   │   │   ├── place.py
│   |   │   │   ├── review.py
│   |   │   │   ├── amenity.py
│   |   │   |   ├── place_amenity
│   |   │   ├── persistence/
│   |   │   |   ├── __init__.py
│   |   │   │   ├── repository.py
│   |   │   ├── script_sql/
│   |   │   ├   ├── services/
|   |   |   |   |   |1_activate_foreign_key.sql
|   |   |   |   |   |2_create_tables.sql
|   |   |   |   |   |3_insert_initial_data_admin
|   |   |   |   |   |insert_initial_data.py
│   |   │   ├── services/
│   |   │   |   ├── __init__.py
│   |   │   │   ├── facade.py
│   |   │   ├── tests/
│   |   │   ├── routes/
│   |   │   ├── swagger/
│   |   ├── instance/
│   |   │   ├── development.db
│   |   │   ├── config.py
|   |   ├── config.py
|   |   ├── run.py
│   |   ├── requirements.txt
|   |   ├── __init__.py
├── .github/
│   ├── workflows/
│   │   ├── test.yml
