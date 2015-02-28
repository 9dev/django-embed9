import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-embed9',
    version='0.3',
    packages=['embed9'],
    include_package_data=True,
    license='MIT License',
    description='Django app that make model objects embeddable on 3rd party websites',
    long_description=README,
    url='https://github.com/9dev/django-embed9',
    author='9dev',
    author_email='9devmail@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
	install_requires = [
		'django >= 1.7.4',
    ],
)
