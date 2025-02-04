
from setuptools import setup

setup(
    name='pycli',
    version='0.1.0',
    py_modules=['pycli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pycli = pycli:cli',
        ],
    },
)
