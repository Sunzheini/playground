"""
You can use the same docker container if you provide a different db name.
need sqlalchemy and psycopg2 packages

You can check status with pgadmin docker container: admin@admin.com, admin -> fastapi_db -> Schema -> public -> Tables -> Users -> Right click -> View/Edit Data
"""
import os
import hashlib
from typing import Optional

from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel, Field
import psycopg2

# ----------------------------------------------------------------------------------------------------
# General Settings
# ----------------------------------------------------------------------------------------------------
DB_NAME = os.getenv("DB_NAME", "fastapi_db")  # Target database name
DB_USER = os.getenv("DB_USER", "postgres_user")  # DB username
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")  # DB password
DB_HOST = os.getenv("DB_HOST", "localhost")  # DB host (localhost for local Docker)
DB_PORT = os.getenv("DB_PORT", "5432")  # DB port (default 5432)

# POSTGRES_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# Get SHA256 hash of a password
def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# ----------------------------------------------------------------------------------------------------
# Function to create the database if it doesn't exist with psycopg2
# ----------------------------------------------------------------------------------------------------
def create_database_if_not_exists() -> bool:
    """Create the database if it doesn't exist. Returns True if DB exists or was created, False on failure."""
    try:
        # Use psycopg2 to connect to the default 'postgres' database with autocommit
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True  # Enable autocommit to allow CREATE DATABASE

        with conn.cursor() as cur:
            # Check if the target database already exists
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
            exists = cur.fetchone()
            if not exists:
                # If not, create the database
                cur.execute(f"CREATE DATABASE {DB_NAME}")
                print(f"Database '{DB_NAME}' created successfully!")
            else:
                print(f"Database '{DB_NAME}' already exists.")
        conn.close()
    except Exception as e:
        print(f"Error: Could not connect to PostgreSQL or create database. Make sure PostgreSQL is running.")
        print(f"Details: {e}")
        return False

    return True


# ----------------------------------------------------------------------------------------------------
# SQLAlchemy for ORM and DB management
# ----------------------------------------------------------------------------------------------------
BASE = declarative_base()   # Base class for ORM models, other models will inherit from this!
DB_ENGINE = create_engine(DATABASE_URL, echo=True)     # SQLAlchemy engine for ORM operations
DB_SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)  # Session factory for DB sessions


# -----------------------------------------------------------------------------------------------------
# Models
# -----------------------------------------------------------------------------------------------------
# Pydantic model
class User(BaseModel):
    """User model representing a user in the system."""
    id: Optional[int] = Field(default=None, ge=1, description="Auto-generated positive integer ID")
    name: str = Field(min_length=1, max_length=100, description="User's full name")
    age: int = Field(ge=0, le=120, description="User's age between 0 and 120")
    city: str = Field(min_length=1, max_length=100, description="City name")
    email: Optional[str] = Field(default=None, description="Valid email address if provided")
    password_hash: Optional[str] = Field(default=None, description="Hashed password")


# SQLAlchemy ORM model
class SQLAlchemyUser(BASE):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)


def create_model_in_db(model_instance):
    """Create a new record in the database for the given model instance."""
    with DB_SESSION_LOCAL() as session_local:     # Create a new session!
        session_local.add(model_instance)
        session_local.commit()
        session_local.refresh(model_instance)
    return model_instance


# -----------------------------------------------------------------------------------------------------
# Action
# -----------------------------------------------------------------------------------------------------
if create_database_if_not_exists():     # try to create DB if it doesn't exist




    create_db_objects()                 # Initialize DB objects

    class User(db_base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False, unique=True)
        age = Column(Integer, nullable=False)
        city = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        password_hash = Column(String, nullable=False)


    # ----------------------------------------------------------------------------------------------------
    def create_db(engine):
        """Create the database tables."""
        db_base.metadata.create_all(bind=engine)  # Create tables defined in ORM models
        print("Database tables created successfully!")

    # Database manager using SQLAlchemy
    class DataBaseManager:
        """A database manager for user data using PostgreSQL and SQLAlchemy."""
        def __init__(self):
            # Ensure tables exist
            create_db(db_engine)
            # Optionally load initial data if table is empty
            with get_db_session() as session:
                if not session.query(User).first():
                    self._load_initial_data(session)

        @staticmethod
        def _load_initial_data(session):
            """Load initial user data into the database."""
            users = [
                User(id=1, name="Alice", age=30, city="New York", email="alice@example.com",
                     password_hash=get_password_hash("pass1")),
                User(id=2, name="Bob", age=25, city="Boston", email="bob@example.com",
                     password_hash=get_password_hash("pass2")),
                User(id=3, name="Charlie", age=35, city="Chicago", email="charlie@example.com",
                     password_hash=get_password_hash("pass3")),
                User(id=4, name="Bubka", age=43, city="Svishtov", email="bubka@example.com",
                     password_hash=get_password_hash("pass4")),
            ]
            session.add_all(users)
            session.commit()

        def get_user_by_username(self, username: str) -> User | None:
            """Retrieve a user by their username from the database."""
            with get_db_session() as session:
                return session.query(User).filter_by(name=username).first()

    # If run as a script, create tables in the database and show example usage
    if __name__ == "__main__":
        create_db(db_engine)

        # Example: Access the database and fetch current timestamp
        with get_db_session() as session:
            result = session.execute(text("SELECT NOW() AS current_time"))
            current_time = result.scalar()
            print(f"Current time from database: {current_time}")

        # Example: Use DataBaseManager to get a user
        db_manager = DataBaseManager()
        user = db_manager.get_user_by_username("Alice")
        if user:
            print(f"Found user: {user.name}, email: {user.email}, city: {user.city}")
        else:
            print("User not found.")
else:
    # If DB creation failed, print error message
    print("Failed to create database. Please check your PostgreSQL connection.")
