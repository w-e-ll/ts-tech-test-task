from setuptools import setup


install_requires = [
    'aiohttp',
    'aiohttp-jinja2',
    'sqlalchemy',
    'aiomysql',
    'Jinja2',
    'PyYAML',
]

setup(
    name='app',
    version='0.1',
    install_requires=install_requires,
)