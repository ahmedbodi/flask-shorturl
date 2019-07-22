from setuptools import setup

setup(
    name='Flask-ShortURL',
    version='1.0',
    license='BSD',
    author='Ahmed Bodiwala',
    author_email='admin@multicoin.co',
    long_description=__doc__,
    packages=['flask_shorturl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
