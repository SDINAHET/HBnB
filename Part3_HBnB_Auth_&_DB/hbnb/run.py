#!/usr/bin/python3
# Main app runner
from flask import Flask
from app import create_app

# Set up the configuration class to use
config_class = "config.DevelopmentConfig"

# Create the Flask application instance using the factory function
app = create_app(config_class=config_class)

if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# from app import create_app
# from app.config import DevelopmentConfig

# app = create_app(DevelopmentConfig)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
