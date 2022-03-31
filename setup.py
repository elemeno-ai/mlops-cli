"""
A CLI with useful commands for interacting with Elemeno ML Ops
"""
from setuptools import find_packages, setup

dependencies = ['click', 'elemeno-ai-sdk==0.0.77']

setup(
    name='elemeno-mlops-cli',
    version='0.0.1',
    url='https://github.com/lucasbmiguel/mlops-cli',
    license='BSD',
    author='Lucas Bonatto Miguel',
    author_email='lucas@elemeno.ai',
    description='A CLI with useful commands for interacting with Elemeno ML Ops',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'mlops = mlops.cli:run',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
