#!/usr/bin/env python
from setuptools import setup

setup(name="scraper",
      version="0.1",
      description="System for testing LED array.",
      url="",
      author="Rory Harpur, Reggie Murphy, Eoin Kenny",
      author_email="rory.harpur@ucdconnect.ie",
      license="GPL3",
      packages=['scraper'],
      entry_points={
          'console_scripts':['scraper = scraper.__main__:main']
          }
    )