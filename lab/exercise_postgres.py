"""
You can use the same docker container if you provide a different db name.
need sqlalchemy and psycopg2 packages

You can check status with pgadmin docker container:
http://localhost:5050/
user: admin@admin.com, pass: admin
-> fastapi_db -> Schema -> public -> Tables -> Users -> Right click -> View/Edit Data

When installed postgres on windows:
Database superuser: postgres
Database password: password
"""
import os
import hashlib
from typing import Optional

from sqlalchemy import create_engine, Column, Integer, String
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
    """Return the SHA256 hash of the given password."""
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
    """Pydantic model for user data."""
    id: Optional[int] = Field(default=None, ge=1, description="Auto-generated positive integer ID")
    name: str = Field(min_length=1, max_length=100, description="User's full name")
    age: int = Field(ge=0, le=120, description="User's age between 0 and 120")
    city: str = Field(min_length=1, max_length=100, description="City name")
    email: Optional[str] = Field(default=None, description="Valid email address if provided")
    password_hash: Optional[str] = Field(default=None, description="Hashed password")


# SQLAlchemy ORM model
class SQLAlchemyUser(BASE):
    """SQLAlchemy ORM model for the users table."""
    __tablename__ = 'users'     # Table name in the database, also this is used to know where to insert the new record
    id = Column(Integer, primary_key=True, autoincrement=True)  # Let DB handle IDs
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)


def pydantic_to_orm(user_model: User) -> SQLAlchemyUser:
    """Convert a Pydantic User model to a SQLAlchemyUser ORM model."""
    return SQLAlchemyUser(
        id=user_model.id,
        name=user_model.name,
        age=user_model.age,
        city=user_model.city,
        email=user_model.email,
        password_hash=user_model.password_hash
    )


def create_tables_from_models() -> None:
    """Create all tables defined in SQLAlchemy models."""
    BASE.metadata.create_all(bind=DB_ENGINE)


def create_user_record_in_a_existing_table(user_data: User) -> SQLAlchemyUser:
    """
    Create a new user record in the database's table.

    user = User(name="John", age=25, city="NYC", email="john@example.com", password_hash="hash123")
    created_user = create_user_record_in_a_existing_table(user)

    :param user_data: User data as a Pydantic model
    :return: The created SQLAlchemyUser ORM instance
    """
    # Convert Pydantic to ORM
    orm_user = pydantic_to_orm(user_data)

    with DB_SESSION_LOCAL() as session:
        session.add(orm_user)
        session.commit()
        session.refresh(orm_user)
    return orm_user


# -----------------------------------------------------------------------------------------------------
# @App Startup - Initialize DB and create tables if needed
# -----------------------------------------------------------------------------------------------------
def initialize_database() -> None:
    """Initialize database and tables."""
    try:
        if create_database_if_not_exists():
            create_tables_from_models()
            print("Database setup complete!")
    except Exception as e:
        print(f"Database initialization failed: {e}")


# ----------------------------------------------------------------------------------------------------
class DataBaseManager:
    """A database manager for user data using PostgreSQL and SQLAlchemy."""
    def __init__(self):
        initialize_database()
        self._load_initial_data_if_empty()

    def _load_initial_data_if_empty(self):
        """Load initial user data if database is empty."""
        with DB_SESSION_LOCAL() as session:

            user_count = session.query(SQLAlchemyUser).count()
            if user_count == 0:
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

        orm_users = [pydantic_to_orm(u) for u in users]   # convert to ORM models
        session.add_all(orm_users)
        session.commit()

    @staticmethod
    def get_user_by_username(username: str) -> SQLAlchemyUser  | None:
        """Retrieve a user by their username from the database."""
        with DB_SESSION_LOCAL() as session:
            return session.query(SQLAlchemyUser).filter_by(name=username).first()


if __name__ == "__main__":
    db_manager = DataBaseManager()

    user = db_manager.get_user_by_username("Alice")
    print(f"Found user: {user.name if user else 'None'}")
