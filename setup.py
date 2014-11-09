from setuptools import setup

setup(name='fixture-generator',
      version='0.1',
      description='Generate league fixture tables.',
      long_description=open('README.rst').read(),
      url='https://MrDubya@bitbucket.org/MrDubya/fixture-generator',
      author='Mike Williams',
      author_email='mrmrdubya@gmail.com',
      license='ISC',
      packages=['fixture_generator'],
      scripts=['bin/fixgen'],
      include_package_data=True,
      zip_safe=False)
