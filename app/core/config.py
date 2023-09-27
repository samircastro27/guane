from functools import lru_cache
from typing import Any, Dict, List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application.
    """

    #: The application name
    APP_NAME: str = "Kyrk Gateway"
    #: The application version
    APP_VERSION: str = "0.0.1"
    #: The application debug mode
    DEBUG: bool = False
    #: The application api version
    API_V1_STR: str = "/api/v1"

    #: Database Service
    DATABASE_SERVICE: str = 'http://kyrk-database.kyrk.svc.cluster.local/'

    #: Exceptions
    EXCEPTIONS: dict = {
        "es": {
            400: "Solicitud al servidor incorrecta",
            401: "No autorizado",
            403: "Metodo incorrecto o no permitido",
            404: "No encontrado",
            409: "Conflicto con los datos ingresados",
            422: "Entidad en el esquema no procesable",
            500: "Error interno del servidor",
            "log": "Nombre de usuario o contraseña incorrecta",
            "magaya": "Usuario de magaya no existe",
        },
        "en": {
            400: "Bad request",
            401: "Not authorized",
            403: "Method not allowed",
            404: "Not found",
            409: "Conflict with entered data",
            422: "Unprocessable Entity",
            500: "Internal server error",
            "log": "Incorrect username or password",
            "magaya": "Magaya user does not exist",
        },
    }

    API_FIREBASE_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'

    API_FIREBASE_KEY: str = 'key'
    
    LEGACY_SERVICE: str = 'http://kyrk-engine.kyrk.svc.cluster.local/'

    RESULTS_SERVICE: str = 'http://kyrk-results-db.kyrk.svc.cluster.local/'


@lru_cache()
def get_settings() -> BaseSettings:
    """Get the settings for the application."""
    return Settings()


settings: Settings = Settings()
