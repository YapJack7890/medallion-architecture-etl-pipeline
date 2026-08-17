from sqlalchemy import create_engine

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "brazilian_ecommerce_dw",
    "user": "postgres",
    "password": "password"
}

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
    f"/{DB_CONFIG['database']}"
)

engine = create_engine(DATABASE_URL)