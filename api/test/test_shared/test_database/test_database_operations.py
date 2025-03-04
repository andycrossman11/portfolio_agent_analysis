import pytest
from unittest.mock import patch, MagicMock
from uuid import uuid4
from datetime import datetime
from shared.database.database_operations import DatabaseOperations
from shared.database.models.pydantic_model_map import Position
from shared.database.models.db_models import PositionSchema

class TestDatabaseOperations:
    @pytest.fixture(scope='module')
    def db_operations(self):
        with patch('shared.database.database_operations.DatabaseSessionFactory') as mock_db_session_factory:
            mock_session = MagicMock()
            mock_db_session_factory.get_session.return_value.__enter__.return_value = mock_session
            db_ops = DatabaseOperations(mock_db_session_factory)
            yield db_ops, mock_session

    def test_create_position(self, db_operations):
        db_ops, mock_session = db_operations
        mock_position = MagicMock(spec=PositionSchema)
        mock_session.add.return_value = None
        mock_session.commit.return_value = None
        mock_session.refresh.return_value = None
        mock_session.query.return_value.filter.return_value.first.return_value = mock_position
        mock_position.id = uuid4()
        mock_position.ticker = "AAPL"
        mock_position.quantity = 10.0
        mock_position.total_purchase_price = 1500.0
        mock_position.purchase_date = datetime.now()

        with patch('shared.database.database_operations.PositionModelConversion.sqlalchemy_to_pydantic', return_value=mock_position):
            position = db_ops.create_position("AAPL", 10.0, 1500.0, datetime.now())
            assert position == mock_position
            mock_session.add.assert_called_once()
            mock_session.commit.assert_called_once()
            mock_session.refresh.assert_called_once()

    def test_get_position(self, db_operations):
        db_ops, mock_session = db_operations
        mock_position = MagicMock(spec=PositionSchema, autospec=True)
        mock_position.id = uuid4()

        mock_session.query.return_value.filter.return_value.first.return_value = mock_position

        with patch('shared.database.database_operations.PositionModelConversion.sqlalchemy_to_pydantic', return_value=mock_position):
            position_id = uuid4()
            position = db_ops.get_position(position_id)
            assert position == mock_position

    def test_get_all_positions(self, db_operations):
        db_ops, mock_session = db_operations
        mock_positions = [MagicMock(spec=PositionSchema) for _ in range(3)]
        mock_session.query.return_value.all.return_value = mock_positions

        with patch('shared.database.database_operations.PositionModelConversion.sqlalchemy_to_pydantic', side_effect=mock_positions):
            positions = db_ops.get_all_positions()
            assert positions == mock_positions

    def test_update_position(self, db_operations):
        db_ops, mock_session = db_operations
        mock_position = MagicMock(spec=PositionSchema)
        mock_session.query.return_value.filter.return_value.first.return_value = mock_position

        with patch('shared.database.database_operations.PositionModelConversion.sqlalchemy_to_pydantic', return_value=mock_position):
            position_id = uuid4()
            updated_position = db_ops.update_position(position_id, "AAPL", 20.0, 3000.0, datetime.now())
            assert updated_position == mock_position

    def test_delete_position(self, db_operations):
        db_ops, mock_session = db_operations
        mock_position = MagicMock(spec=PositionSchema)
        mock_session.query.return_value.filter.return_value.first.return_value = mock_position

        position_id = uuid4()
        result = db_ops.delete_position(position_id)
        assert result is True

    def test_delete_position_not_found(self, db_operations):
        db_ops, mock_session = db_operations
        mock_session.query.return_value.filter.return_value.first.return_value = None

        position_id = uuid4()
        result = db_ops.delete_position(position_id)
        assert result is False