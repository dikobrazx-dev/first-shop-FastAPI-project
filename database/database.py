from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database/SQLiteDataBase.db")
SessionLocal = sessionmaker(bind = engine)
def get_session():
    with SessionLocal as session:
        yield session
