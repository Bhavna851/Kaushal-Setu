# app/models.py
from app import db
from datetime import datetime

class User(db.Model):
    """
    1. THE USER TABLE (Authentication)
    This table handles account credentials for logging in.
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)  # Securely stored encrypted password
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relational Link: Connects one User to their Profile details
    profile = db.relationship('Profile', backref='user', uselist=False, cascade="all, delete-orphan")
    
    # Relational Link: Connects one User to all their historical application logs
    applications = db.relationship('ApplicationTracker', backref='user', cascade="all, delete-orphan")


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        unique=True,
        nullable=False
    )

    phone = db.Column(db.String(20))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(20))

    education = db.Column(db.String(100))
    college = db.Column(db.String(150))
    branch = db.Column(db.String(100))
    graduation_year = db.Column(db.String(10))

    skills = db.Column(db.Text)

    city = db.Column(db.String(100))
    state = db.Column(db.String(100))

    linkedin = db.Column(db.String(255))
    github = db.Column(db.String(255))

    bio = db.Column(db.Text)

    resume_filename = db.Column(db.String(255))
    

class Internship(db.Model):
    """
    3. THE INTERNSHIP TABLE (Corporate Openings Database)
    This stores the vacancies that our AI-Light system evaluates against.
    """
    __tablename__ = 'internships'
    
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    sector = db.Column(db.String(100), nullable=False)       # e.g., "IT", "Banking", "Manufacturing"
    
    required_skills = db.Column(db.Text, nullable=False)     # e.g., "Excel, Typing"
    required_education = db.Column(db.String(100), nullable=False) 
    
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    stipend = db.Column(db.Integer, default=0)                # Monthly allowance
    platform = db.Column(db.String(100))
    apply_link = db.Column(db.String(500))


class ApplicationTracker(db.Model):
    """
    4. THE APPLICATION TRACKER TABLE (State Persistence)
    Remembers which internships the user clicked "Apply" on.
    """
    __tablename__ = 'application_tracker'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'), nullable=False)
    
    status = db.Column(db.String(50), default="Applied")     # Status states: "Applied", "Under Review", "Selected"
    applied_on = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Fetch job details instantly when looking at application logs
    internship = db.relationship('Internship')