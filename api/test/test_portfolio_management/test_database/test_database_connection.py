import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from src.portfolio_management.database.database_connection import DatabaseSessionFactory

class TestDatabaseSessionFactory:
    @pytest.fixture(scope='module')
    def db_session_factory(self):
        with patch('src.portfolio_management.database.database_connection.create_engine') as mock_create_engine:
            mock_engine = MagicMock()
            mock_create_engine.return_value = mock_engine
            factory = DatabaseSessionFactory()
            yield factory

    def test_database_url(self, db_session_factory):
        expected_url = "postgresql+psycopg2://portfolio_manager:portfolio_manager@localhost:5555/portfolio"
        assert db_session_factory.database_url == expected_url

    def test_get_session(self, db_session_factory):
        with patch.object(db_session_factory, 'SessionLocal', return_value=MagicMock(spec=Session)) as mock_session_local:
            with db_session_factory.get_session() as session:
                assert session is mock_session_local.return_value
                mock_session_local.return_value.close.assert_not_called()
            mock_session_local.return_value.close.assert_called_once()