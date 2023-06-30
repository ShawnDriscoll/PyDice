
from setuptools import setup, find_packages

setup(

    ### Metadata

    name='pydice',

    version='3.12.5',

    description='A Python 3.11 module that your game code calls to make dice rolls.',

    url='https://github.com/ShawnDriscoll/pydice/tree/master/rpg_tools',

    download_url='',

    license='MIT',

    author='Shawn Driscoll',
    author_email='shawndriscoll@hotmail.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Natural Language :: English',
        'Operating System :: Windows 10',
        'Operating System :: Windows 11',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Build Tools',
    ],

    ### Dependencies

    install_requires=[],

    ### Contents

    packages=find_packages()
    )