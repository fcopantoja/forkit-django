from setuptools import find_packages, setup


BASE_PACKAGE = 'forkit'
version = __import__(BASE_PACKAGE).get_version()


setup(
    version=version,
    name='forkit-django',
    author='Virtualstock',
    author_email='dev.admin@virtualstock.com',
    description='Utility functions for forking, resetting and diffing model objects',
    license='BSD',
    keywords='fork deepcopy model abstract diff',
    packages=find_packages(exclude=['forkit.tests']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
