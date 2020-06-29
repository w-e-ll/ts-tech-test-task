import pytest

from app.main import init_app
from app.settings import BASE_DIR, get_config
from init_db import (
    setup_db,
    create_tables,
    sample_data,
    drop_tables
)

TEST_CONFIG_PATH = BASE_DIR / 'config' / 'config_test.yaml'
TEST_CONFIG = TEST_CONFIG_PATH.as_posix()

@pytest.fixture
async def cli(test_client):
    app = await init_app()
    return await test_client(app)


@pytest.fixture(scope='module')
def db():
    test_config = get_config(TEST_CONFIG)
    setup_db(test_config['mysql'])
    yield
    teardown_db(test_config['mysql'])


@pytest.fixture
def tables_and_data():
    create_tables()
    sample_data()
    yield
    drop_tables()