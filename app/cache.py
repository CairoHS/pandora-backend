from functools import lru_cache
import config

@lru_cache
def pega_settings():
    return config.Settings()