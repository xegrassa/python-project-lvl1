# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['brain_games', 'brain_games.scripts']

package_data = \
{'': ['*']}

install_requires = \
['prompt>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['brain-even = brain_games.scripts.brain_even:main',
                     'brain-games = brain_games.scripts.brain_games:main']}

setup_kwargs = {
    'name': 'xegrassa-brain-games',
    'version': '1.0.2',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.8,<4.0.0',
}


setup(**setup_kwargs)
