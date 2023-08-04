from setuptools import setup

setup(name='fixture-generator',
      version='0.2',
      description='Generate league fixture tables.',
      long_description=open('README.rst').read(),
      url='https://github.com/mrdubya/fixture-generator.git',
      author='Mike Williams',
      author_email='mrmrdubya@gmail.com',
      license='ISC',
      packages=['fixture_generator'],
      scripts=['bin/fixgen', 'bin/fixgen.bat'],
      include_package_data=True,
      zip_safe=False)
