try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='QSTK',
    version='0.1',
    description='Python toolkit for stocks',
    author='Tucker Balch',
    author_email='tucker@cc.gatech.edu',
    url='http://wiki.quantsoftware.org/','
    install_requires=[
        'nose',
    ],
    tests_require=[
    ],
    setup_requires=[],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
)
