from setuptools import setup

setup(
    name="dirtrace",
    version="0.0.3",
    description="generate chromium's trace event format json file from directory content file size",
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
    zip_safe=False
)
