from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dirtrace",
    version="0.0.5",
    description="generate chromium's trace event format json file from directory content file size",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/everettjf/dirtrace",
    author="everettjf",
    author_email="everettjf@live.com",
    license='MIT',
    packages=["dirtrace"],
    entry_points="""
         [console_scripts]
         dirtrace = dirtrace.dirtrace:main
    """,
    install_requires=[
    ],
    zip_safe=False,
)
