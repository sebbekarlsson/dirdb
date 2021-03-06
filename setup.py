from setuptools import setup


setup(
    name='dirdb',
    version='1.0',
    install_requires=[
        'graphql-py'
    ],
    packages=[
        'dirdb'
    ],
    entry_points={
        "console_scripts": [
            'dirdb = dirdb.bin:run',
            'dirdb-client = dirdb.bin:run_client'
        ]
    }
)
