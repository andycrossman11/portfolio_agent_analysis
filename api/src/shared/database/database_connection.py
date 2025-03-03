from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
import os
from typing import Generator
from contextlib import contextmanager

class DatabaseSessionFactory:
    def __init__(self) -> None:
        db_user: str = os.getenv("POSTGRES_USER", "portfolio_manager")
        db_password: str = os.getenv("POSTGRES_PASSWORD", "portfolio_manager")
        db_host: str = os.getenv("POSTGRES_HOST", "postgres-api")
        db_port: str = os.getenv("POSTGRES_PORT", "5432")
        db_name: str = os.getenv("POSTGRES_DB", "portfolio")
        
        self.database_url: str = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        
        self.engine = create_engine(self.database_url, echo=True)
        self.SessionLocal = scoped_session(sessionmaker(bind=self.engine, autocommit=False, autoflush=False))

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """Provide a new database session."""
        session: Session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()
