import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-versionator",
    version="1.1.0",
    author="AlexCLeduc",
    # author_email="author@example.com",
    # description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexCleduc/django-versionator",
    packages=[
        # find_packages() also includes extraneous stuff, like testing and sample_app
        package
        for package in setuptools.find_packages()
        if package.startswith("versionator")
    ],
    install_requires=[],
    # to install these subdeps, use pip install django-versionator[changelog]
    extras_require={
        "changelog": [
            "pleasant-promises>=1.1",
            "graphene>=3.1.1, <4",
            "graphene-django>=3, <4",
            "graphql-core-promise>=3.2.3,<4",
        ],
    },
    tests_require=["django"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
