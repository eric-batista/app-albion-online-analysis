import pathlib
import socket

from devtools.config import Config
from devtools.providers.config import from_env
from devtools.providers.database import DatabaseConfig, Driver

config = Config()


ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE_DIR = ROOT.parent

# APP SETUP
BASE_PATH = config("BASE_PATH", str)
APP_ENVIRONMENT = config("APP_ENVIRONMENT", str, "dev")
APP_APPLICATION = config("APP_APPLICATION", str, "app-albion-accounting")
HOSTNAME = config("HOSTNAME", str, socket.gethostname())
HOST = config("APP_DEFAULT_HOST", str, "0.0.0.0")
PORT = config("APP_DEFAULT_PORT", int, 8000)

DB_DRIVER = config("DB_DRIVER", Driver, Driver.POSTGRES)

BASE_AO_PRICES_DATA_API = config("BASE_AO_PRICES_DATA_API", str)
DEFAULT_DATABASE = "postgres"
default_database = from_env(DatabaseConfig, driver=DB_DRIVER)
