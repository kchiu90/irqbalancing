# Reference: Internal rtld_audit repo
# Last Modified: June 7, 2018

import sys
import codecs
import subprocess
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# get git tag used as package version
p = subprocess.Popen('git describe --tags', cwd=here, shell=True, stdout=subprocess.PIPE)
tag, _ = p.communicate()
if p.returncode != 0:
    sys.stderr.write('Could not determine git tag\n')
    sys.exit(1)
tag = tag.strip()

setup(
    name='irqservice',
    version=tag,
    description='IRQ Balance Service',
    url='https://github.com/kuofchiu/irqbalancing',
    author='James Kuo Chiu',
    author_email='kuo.chiu@verizondigitalmedia.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'irqservice=server.irq_server:main',
        ],
    },
)