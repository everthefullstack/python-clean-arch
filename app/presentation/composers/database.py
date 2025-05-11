from app.infra.database.database import DatabaseManager
from app.infra.engine.engine import engine
from app.infra.logger.logger import logger as lg


def create_database():
    lg.info("Executando a função create_database")

    database = DatabaseManager(engine=engine)
    database.create_database()
