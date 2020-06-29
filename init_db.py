# polls/init_db.py
from sqlalchemy import create_engine, MetaData

from app.settings import config, BASE_DIR, get_config

from app.db import terminal


DSN = "mysql://{user}:{password}@{host}:{port}/{db}"

ADMIN_DB_URL = DSN.format(
    user='root', password='', db='mysql',
    host='localhost', port=3306
)

admin_engine = create_engine(ADMIN_DB_URL, isolation_level='AUTOCOMMIT')

USER_CONFIG_PATH = BASE_DIR / 'config' / 'config.yaml'
USER_PATH = USER_CONFIG_PATH.as_posix()
USER_CONFIG = get_config(USER_PATH)
USER_DB_URL = DSN.format(**USER_CONFIG['mysql'])
user_engine = create_engine(USER_DB_URL)

TEST_CONFIG_PATH = BASE_DIR / 'config' / 'config_test.yaml'
TEST_PATH = TEST_CONFIG_PATH.as_posix()
TEST_CONFIG = get_config(TEST_PATH)
TEST_DB_URL = DSN.format(**TEST_CONFIG['mysql'])
test_engine = create_engine(TEST_DB_URL)

def setup_db(config):

    db_name = config['mysql']['db']
    db_user = config['mysql']['user']

    conn = admin_engine.connect()
    conn.execute("DROP DATABASE IF EXISTS %s;" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s;" % db_user)
    conn.execute("CREATE USER '%s'@'localhost';" % db_user)
    conn.execute("CREATE DATABASE %s /*!40100 DEFAULT CHARACTER SET utf8 */;" % db_name)
    conn.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO '%s'@'localhost';" % (db_name, db_user))
    conn.close()


def teardown_db(config):

    db_name = config['db']
    db_user = config['user']

    conn = admin_engine.connect()
    conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s" % db_user)
    conn.close()


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[terminal])


def drop_tables(engine):
    meta = MetaData()
    meta.drop_all(bind=engine, tables=[terminal])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(terminal.insert().values(name='Bob', city='Oakland', age='27'))
    conn.execute(terminal.insert().values(name='Jim', city='NY', age='26'))
    conn.close()


if __name__ == '__main__':

    user_engine = create_engine(USER_DB_URL)
    create_tables(engine=user_engine)
    sample_data(engine=user_engine)

    test_engine = create_engine(TEST_DB_URL)
    create_tables(engine=test_engine)
    sample_data(engine=test_engine)
    
    # drop_tables()