import uuid
from datetime import datetime
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.api import app, StockPurchase
import pytest

client = TestClient(app)

# Mock the entire portfolio_management.database package
@pytest.fixture(scope='module')
def mock_db_ops():
    with patch('src.api.DB_OPS', new_callable=MagicMock) as mock_db_ops:
        yield mock_db_ops

class TestAPI:
    test_id = uuid.uuid4()
    test_position = {
        "id": str(uuid.uuid4()),
        "ticker": "AAPL",
        "quantity": 10.0,
        "total_purchase_price": 1500.0,
        "purchase_date": "02-20-2021",
    }

    def test_create_position(self, mock_db_ops):
        mock_db_ops.create_position.return_value = self.test_position
        response = client.post('/positions', json=self.test_position)
        assert response.status_code == 200
        assert response.json() == self.test_position

    def test_get_positions(self, mock_db_ops):
        mock_db_ops.get_all_positions.return_value = [self.test_position]
        response = client.get('/positions')
        assert response.status_code == 200
        assert response.json() == [self.test_position]

    def test_update_position(self, mock_db_ops):
        mock_db_ops.update_position.return_value = True
        response = client.put(f'/positions/{self.test_id}', json=self.test_position)
        assert response.status_code == 200
        assert response.json() == {"message": "Position updated successfully"}

    def test_update_position_not_found(self, mock_db_ops):
        mock_db_ops.update_position.return_value = False
        response = client.put(f'/positions/{self.test_id}', json=self.test_position)
        assert response.status_code == 404
        assert response.json() == {"detail": "Position not found"}

    def test_delete_position(self, mock_db_ops):
        mock_db_ops.delete_position.return_value = True
        response = client.delete(f'/positions/{self.test_id}')
        assert response.status_code == 200
        assert response.json() == {"message": "Position deleted successfully"}

    def test_delete_position_not_found(self, mock_db_ops):
        mock_db_ops.delete_position.return_value = False
        response = client.delete(f'/positions/{self.test_id}')
        assert response.status_code == 404
        assert response.json() == {"detail": "Position not found"}