from setuptools import setup, find_packages

setup(
    name='django-chart',
    version='dev',
    description='Django chart app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-chart',
    packages = find_packages(),
    include_package_data=True,
)

