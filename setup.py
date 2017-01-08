#!/usr/bin/python3

"""
    This file is part of omdb-tool.

    omdb-tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    omdb-tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with omdb-tool.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='omdb-tool',
      version=version,
      description="Interactive command-line omdb api tool using Python",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='movies omdb imdb',
      author='eplanet',
      author_email='emeric.planet@gmail.com',
      url='https://github.com/eplanet/omdb-tool',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
