#!/usr/bin/env python
from setuptools import setup

if __name__ == '__main__':
    setup(
        name='uetools.plugins.asset_dumper',
        version='0.0.0',
        description='uetools plugin example',
        author='Pierre Delaunay',
        packages=[
            'uetools.plugins.asset_dumper',
        ],
        install_requires=['uetools', 'simple-parsing'],
        setup_requires=['setuptools'],
        zip_safe=False,
        namespace_packages=['uetools.plugins'],
        entry_points={
            "UECLICommands": ["dumper = uetools.plugins.asset_dumper.command:MyNewCommand"],
        },
    )
