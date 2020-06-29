# app/main.py
import logging
import sys

import aiohttp_jinja2
import jinja2

from aiohttp import web
from middlewares import setup_middlewares
from db import close_db, init_db
from routes import setup_routes
from settings import config, BASE_DIR


async def init_app():

    app = web.Application()

    app['config'] = config

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(app,
    	loader=jinja2.FileSystemLoader(str(BASE_DIR / 'app' / 'templates')))

    # create db connection on startup, shutdown on exit
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    # setup views and routes
    setup_routes(app)

    setup_middlewares(app)

    return app


def main():
	logging.basicConfig(level=logging.DEBUG)

	app = init_app()
	web.run_app(app,
				host=config['host'],
				port=config['port'])


if __name__ == '__main__':
    main()
