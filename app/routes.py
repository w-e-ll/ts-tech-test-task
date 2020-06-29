# app/routes.py
import pathlib

from views import index, post_data, success


PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', index,  name='index')
    app.router.add_get('/post/', post_data, name='post-data')
    app.router.add_post('/post/', post_data, name='post-data')
    app.router.add_get('/success/', success, name='success')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')