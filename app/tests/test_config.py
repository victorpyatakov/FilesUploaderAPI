from app.config import Settings


class TestConfig:
    def test_settings_creation(self):
        settings = Settings()
        assert settings.upload_dir == "test_upload_dir"
