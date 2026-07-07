# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'sih_secret_key_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pm_internship.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    import os

    with app.app_context():
        print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])
        print("Instance path:", app.instance_path)
        print("Current working directory:", os.getcwd())
    
    
        from app import models
        db.create_all()

        from app.models import Internship
        print("Internships in DB:", Internship.query.count())

     # Register Blueprint
    from app.routes import main_blueprint
    app.register_blueprint(main_blueprint)
        
    return app