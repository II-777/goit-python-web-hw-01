from setuptools import setup, find_namespace_packages

setup(name='infinity',
      version='0.1.0',
      description='command line assistant with notetaking and addressbook functions.',
      url='https://github.com/II-777/Infinity',
      author='II-777',
      author_email='777dev0@protonmail.com',
      license='MIT',
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],

      include_package_data=True,
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['infinity = infinity.main:main']},
      install_requires=[
              'rich==13.7.0',
      ]
      )
