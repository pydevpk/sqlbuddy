from setuptools import find_packages, setup

setup(
    name='sqlbuddy',
    packages=find_packages(include=['sqlbuddy']),
    version='0.1.2',
    description='A SQL library for generating SQL queries using GPT-3.5',
    author='Pradeep Kumar Yadav',
    install_requires=['openai'],
    author_email='pydev.pk@gmail.com'
)