"""Require running database server"""

from app.db import terminal


async def test_index(cli):
    response = await cli.get('/')
    assert response.status == 200
    assert 'Main' in await response.text()


async def test_post_data(cli):
    response = await cli.get('/post/')
    assert response.status == 200
    assert 'saved and processed' in await response.text()