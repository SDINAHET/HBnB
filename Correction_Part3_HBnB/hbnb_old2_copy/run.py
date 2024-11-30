from app import create_app

# Initialisation de l'application Flask
app = create_app()

if __name__ == "__main__":
    # Lancement de l'application sur localhost, port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
