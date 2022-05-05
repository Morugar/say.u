from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DATABASE_URL

def main():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())

    session.close()

if __name__ == '__main__':
    main()