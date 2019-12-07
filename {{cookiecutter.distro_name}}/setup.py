# -*- coding: utf-8 -*-

# NOTE: This file is just for compatibility only. Use pyproject.toml
# instead.
# (currently pip doesn't support editable mode with pyproject.toml)

from distutils.core import setup

package_dir = \
    {'': 'src'}

packages = \
    ['{{cookiecutter.package_name}}']

package_data = \
    {'': ['*']}

setup_kwargs = {
    'name': '{{cookiecutter.distro_name}}',
    'version': '{{cookiecutter.version}}',
    'description': '{{cookiecutter.description}}',
    'long_description': None,
    'author': '{{cookiecutter.author}}',
    'author_email': '{{cookiecutter.author_email}}',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
