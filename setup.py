# This is a Python script that contains the configuration information for building and distributing a Python package.
# It typically includes information such as the package name, version, author, and dependencies.
# It can also specify scripts to be installed with the package, and other package-specific options.

from setuptools import find_packages, setup

setup(
    author="Breno Farias",
    version="0.0.1",
    name="heart_disease_risk",
    packages=find_packages(exclude=["heart_disease_risk_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
