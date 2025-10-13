"""
You can use the same docker container if you provide a different db name.
need sqlalchemy and psycopg2 packages
"""
import os
from sqlalchemy import create_engine, text  # SQLAlchemy for DB connection and SQL execution
from sqlalchemy.orm import declarative_base, sessionmaker  # ORM base and session maker
import psycopg2  # Add psycopg2 for direct DB connection

# Get DB connection details from environment variables or use defaults
DB_NAME = os.getenv("DB_NAME", "fastapi_db")  # Target database name
DB_USER = os.getenv("DB_USER", "postgres_user")  # DB username
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")  # DB password
DB_HOST = os.getenv("DB_HOST", "localhost")  # DB host (localhost for local Docker)
DB_PORT = os.getenv("DB_PORT", "5432")  # DB port (default 5432)

# Connection string for default 'postgres' database (needed to create new DB)
POSTGRES_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"


def create_database_if_not_exists():
    """Create the database if it doesn't exist"""
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
        # Handle connection errors (e.g., PostgreSQL not running)
        print(f"Error: Could not connect to PostgreSQL or create database. Make sure PostgreSQL is running.")
        print(f"Details: {e}")
        return False

    return True  # Return True if DB exists or was created


# Try to create the database first
if create_database_if_not_exists():

    # Build connection string for the target database
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Create SQLAlchemy engine for ORM operations
    db_engine = create_engine(DATABASE_URL)

    # Create a session factory for DB sessions
    db_session_local = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

    # Base class for ORM models
    db_base = declarative_base()

    # User ORM model matching your in-memory structure
    from sqlalchemy import Column, Integer, String
    try:
        from routers.security import get_password_hash  # Assumes you have this function
    except ImportError:
        # Fallback: simple hash for demonstration
        import hashlib
        def get_password_hash(password: str) -> str:
            return hashlib.sha256(password.encode()).hexdigest()

    class User(db_base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False, unique=True)
        age = Column(Integer, nullable=False)
        city = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        password_hash = Column(String, nullable=False)

    def get_db_session():
        """
        Returns a SQLAlchemy session connected to the fastapi_db database.
        Usage:
            with get_db_session() as session:
                # perform queries, inserts, etc.
        """
        return db_session_local()

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
