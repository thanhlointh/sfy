"""
Database session management
"""

from contextlib import contextmanager

from sqlmodel import Session, create_engine
from src.settings.general import DBSettings

# print(DBSettings().db_url)
engine = create_engine(url=DBSettings().db_url)

def get_session():
    """
    """
    with Session(engine) as session:
        yield session


@contextmanager
def get_session_context():
    """
    """
    db: Session = Session(engine)
    try:
        yield db
    finally:
        db.close()