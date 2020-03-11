import setuptools

setuptools.setup(
    name="tostring",
    version="0.1.0",
    packages=setuptools.find_packages(),
    description="Translate Python built-in types into their string equivalents.",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RDIL/tostring",
    keywords="to string python builtins"
)
