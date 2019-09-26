#!/usr/bin/env python
import io
import re
import sys

from setuptools import find_packages, setup

with io.open('./humanverse/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='humanverse',
    version=version,
    description='We do not read and write poetry because it is cute. We read and write poetry because we are members of the human race..',
    long_description=long_description,
    author='Philip James',
    author_email='phildini@galaxybrain.io',
    license='Apache Software License',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'Human. Verse.',
            'bundle': 'co.galaxybrain.humanverse'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
                'toga-cocoa==0.3.0.dev11',
            ]
        },
        'linux': {
            'app_requires': [
                'toga-gtk==0.3.0.dev11',
            ]
        },
        'windows': {
            'app_requires': [
                'toga-winforms==0.3.0.dev11',
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
                'toga-ios==0.3.0.dev11',
            ]
        },
        'android': {
            'app_requires': [
                'toga-android==0.3.0.dev11',
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
                'toga-django==0.3.0.dev11',
            ]
        },
    }
)
