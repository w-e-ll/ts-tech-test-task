# app/views.py
import aiohttp
import aiohttp_jinja2
import asyncio
import db

from aiohttp import web
from validate import validate_form


def redirect(router, route_name):
    location = router[route_name].url_for()
    return web.HTTPFound(location)


@aiohttp_jinja2.template('index.html')
async def index(request):
	async with request.app['db'].acquire() as conn:
		result = await db.get_data(conn)
		users = [dict(row) for row in result]
		return {"users": users}
 

@aiohttp_jinja2.template('post_data.html')
async def post_data(request):
	if request.method == 'POST':
		form = await request.post()
		async with request.app['db'].acquire() as conn:
			error = await validate_form(conn, form)
			if error:
				return {'error': error}
			else:
				data = await db.post_data(conn, form['name'], form['city'], form['age'])
				if data:
					await asyncio.sleep(10)
					raise redirect(request.app.router, 'success')
					await asyncio.sleep(10)
					raise redirect(request.app.router, 'index')
	return {}


@aiohttp_jinja2.template('success.html')
async def success(request):
	return {'success' : 'saved and processed'}