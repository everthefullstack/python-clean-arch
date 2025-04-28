from app.infra.engine.engine import engine
from app.infra.database.database import DatabaseManager


def create_database():
    
    database: DatabaseManager = DatabaseManager(engine=engine)
    database.create_database()
    