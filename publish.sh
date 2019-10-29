
# how to publish python package
# https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi
# pip install --user --upgrade twine

twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose
