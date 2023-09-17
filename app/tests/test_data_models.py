import pytest
from pydantic import ValidationError

from app.data_models import FileInfo


class TestDataModels:
    def test_valid_file_info(self):
        data = {"guid": "1234-5678-1234-5678", "name": "test.txt"}
        file_info = FileInfo(**data)
        assert file_info.guid == data["guid"]
        assert file_info.name == data["name"]

    def test_invalid_file_info(self):
        invalid_data = {"guid": 12345, "name": 12345}
        with pytest.raises(ValidationError):
            FileInfo(**invalid_data)
