from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env',
                                      env_file_encoding="utf-8")

    ENDERECO_BANCO: str
    CHAVE_SECRETA: str
    ALGORITMO: str
    HORAS_PARA_EXPIRAR_REFRESH_TOKEN: int
    MINUTOS_PARA_EXPIRAR_ACESS_TOKEN: int

settings = Settings()