import os
import pathlib

import sqlalchemy.orm
from util import db
import sqlalchemy

def cv_handler(cv_path):
    """CV test data directory handler

    Args:
        cv_path (Path): Path to cv test
    """    
    print(f"Processing CV files: {cv_path}")

def main():
    data_directory = 'data'
    db_filename = 'sensor_data.db'
    db_path = os.path.join(data_directory, db_filename)

    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    # Create database engine with SQLite
    engine = sqlalchemy.create_engine(f'sqlite:///{db_path}', echo=True)

    # Create tables
    db.Base.metadata.create_all(engine)
    print('Tables set.')

    # Creata a session
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    try:
        test_types = ['cv', 'oltf', 'Q', 'noise']
        for tt_name in test_types:
            existing_tt = session.query(db.TestType).filter_by(name=tt_name).first()
            if not existing_tt:
                new_tt = db.TestType(name=tt_name)
                session.add(new_tt)
                print(f"Add test type: {tt_name}")
        session.commit()
        
        data_path = pathlib.Path(data_directory)

        for date_dir in data_path.iterdir():
            if date_dir.is_dir():
                print(f"\nProcessing directory: {date_dir}")

                for sub_dir in test_types:
                    

    except Exception as e:
        session.rollback()
        print(f"Exception occurs, rolling back: {e}")
    finally:
        session.close()
        print("Session closed.")

if __name__ == "__main__":
    main()
