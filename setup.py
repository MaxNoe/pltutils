from setuptools import setup

setup(name='pltutils',
      version='0.1',
      description='a small collection of convenience wrappers for matplotlib',
      url='http://github.com/MaxNoe/pltutils',
      author='Maximilian Nöthe',
      author_email='maximilian.noethe@tu-dortmund.de',
      license='MIT',
      packages=['pltutils'],
      install_requires=[
          'matplotlib',
      ],
      zip_safe=False)
