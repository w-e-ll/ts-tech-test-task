import aiomysql.sa

from sqlalchemy import (
    Table, Column, Integer, 
    String, MetaData
)


__all__ = ['terminal']

metadata = MetaData()

terminal = Table(
    'terminal', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(200), nullable=False),
    Column('age', Integer, nullable=False),
    Column('city', String(200), nullable=False)
)


async def init_db(app):
    conf = app['config']['mysql']
    engine = await aiomysql.sa.create_engine(
        user=conf['user'], 
        db=conf['db'], 
        host=conf['host'], 
        password=str(conf['password'])
    )
    app['db'] = engine
    return engine


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()


async def get_data(conn):
    async with conn.execute(terminal.select()) as result:
        return await result.fetchall()


async def post_data(conn, name, city, age):
    obj = terminal.insert().values(name=name, city=city, age=age)
    await conn.execute(obj)
    await conn.execute("commit")
    return obj.compile().params



    