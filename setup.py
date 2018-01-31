from setuptools import setup


setup(
    name='dirdb',
    version='1.0',
    install_requires=[
        ''
    ],
    packages=[
        'dirdb'
    ],
    entry_points={
        "console_scripts": [
            "dirdb = dirdb.bin:run"
        ]
    }
)
