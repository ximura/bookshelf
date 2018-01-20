from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='bookshelf',
      version='1.0',
      description='experiment with goodread api',
      author='ximura',
      author_email='',
      url='',
      packages=find_packages(exclude=['test', 'test.*']),
      python_requires='>=3.6',
      install_requires=install_requires
      )
