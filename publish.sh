
# how to publish python package
# https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi
# pip install --user --upgrade setuptools wheel
# pip install --user --upgrade twine

rm -rf dist

python setup.py sdist bdist_wheel

twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose
