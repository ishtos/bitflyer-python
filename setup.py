from setuptools import setup, find_packages


requires = ["requests"]

setup(
    name="bitflyer-python",
    version="0.0.1",
    description="wrapper library for bitflyer api",
    author="ishtos",
    author_email="ginkgonut.9960@gmail.com",
    license="Apache 2.0",
    packages=find_packages(where="src"),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python"
    ],
)
