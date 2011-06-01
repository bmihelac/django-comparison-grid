from setuptools import setup, find_packages
import os


VERSION = __import__("grid").__version__

setup(
    name="django-comparison-grid",
    description="Django application allows creating comparison grids",
    long_description=open(os.path.join(os.path.dirname(__file__), 
        'README.rst')).read(),
    version=VERSION,
    author="Bojan Mihelac",
    author_email="bmihelac@mihelac.org",
    url="https://github.com/bmihelac/django-comparison-grid",
    packages=find_packages(exclude=["example", "example.*"]),
)

