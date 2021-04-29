from dotenv import load_dotenv
from os import getenv


load_dotenv()

database = {
    "username": getenv("USERNAME", "sahar"),
    "password": getenv("PASSWORD", "Aa123456"),
    "host": getenv("HOST", "db"),
    "db_name": getenv("DB_NAME", "SitesChecker"),
    "port": int(getenv("PORT", 1433)),
}
