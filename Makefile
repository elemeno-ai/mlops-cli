.PHONY: clean wheel pip-pypi bump

clean:
	rm -rf dist

wheel:
	python setup.py bdist_wheel

_pip-pypi: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*.whl

pip-pypi: clean _pip-pypi

bump:
	bumpversion --new-version $(version) patch --verbose