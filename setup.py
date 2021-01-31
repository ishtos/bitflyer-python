from setuptools import setup


requires = ["requests"]

setup(
    name="bitflyer-py",
    version="0.0.5",
    url="https://github.com/ti-ginkgo/bitflyer-python",
    description="wrapper library for bitflyer api",
    author="ishtos",
    author_email="ginkgonut.9960@gmail.com",
    license="MIT",
    packages=["bitflyer"],
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python"
    ],
    keywords=["bitflyer"],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)
