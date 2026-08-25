from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Сервис для поддержки котиков'
    database_url: str = 'sqlite+aiosqlite:///./cat-charity.db'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
