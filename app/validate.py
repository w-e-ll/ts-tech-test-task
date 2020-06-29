import db


async def validate_form(conn, form):

	name = form['name']
	city = form['city']
	age = form['age']

	if not name:
		return 'name is required'
	if not city:
		return 'city is required'
	if not age:
		return 'age is required'
	else:
		return None

	return 'error'