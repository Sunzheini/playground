from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()   # It creates a base class that your ORM models will inherit from

class User(Base):
    __tablename__ = 'users'  # Name of the table in the database

    id = Column(Integer, primary_key=True)   # Primary key column
    name = Column(String)                    # Name column
    age = Column(Integer)                    # Age column


# Database connection string (using SQLite for simplicity)
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL, echo=True)     # echo=True for SQL query logging
Base.metadata.create_all(engine)                    # Create tables based on the defined models
Session = sessionmaker(bind=engine)                 # Create a configured "Session" class


def main():
    session = Session()  # Create a new session

    # Create
    new_user = User(name='Alice', age=30)
    session.add(new_user)
    session.commit()  # Commit the transaction to save the new user

    # Read
    user = session.query(User).filter_by(name='Alice').first()
    print(f'Retrieved User: {user.name}, Age: {user.age}')

    # Update
    user.age = 31
    session.commit()  # Commit the transaction to save the changes

    # Delete
    session.delete(user)
    session.commit()  # Commit the transaction to delete the user

    session.close()  # Close the session
