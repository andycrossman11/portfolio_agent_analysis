from .database_connection import DatabaseSessionFactory
from .database_operations import DatabaseOperations
from .models.pydantic_model_map import Position, Analysis

db_factory: DatabaseSessionFactory = DatabaseSessionFactory()

DB_OPS: DatabaseOperations = DatabaseOperations(db_factory)
