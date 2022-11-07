from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from backend.localsettings import postgresql
from sqlalchemy.ext.declarative import declarative_base

def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


engine = get_engine(postgresql["pguser"],
                    postgresql["pgpassword"],
                    postgresql["pghost"],
                    postgresql["pgport"],
                    postgresql["pgdb"])


def get_engine_from_postgresql():
    keys = ["pguser", "pgpassword", "pghost", "pgport", "pgdb"]
    if not all(key in keys for key in postgresql.keys()):
        raise Exception("Bad config file")

    return get_engine(postgresql["pguser"],
                    postgresql["pgpassword"],
                    postgresql["pghost"],
                    postgresql["pgport"],
                    postgresql["pgdb"])


def get_session():
    engine = get_engine_from_postgresql()
    session = sessionmaker(bind=engine)()
    return session

session = get_session()
Base = declarative_base()