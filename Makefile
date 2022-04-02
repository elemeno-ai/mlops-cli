.PHONY: clean wheel pip-pypi bump

clean:
	rm -rf dist

wheel:
	python setup.py bdist_wheel

_pip-pypi: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*.whl

pip-pypi: clean _pip-pypi

bump-custom:
	bumpversion --new-version $(version) patch --verbose

bump-patch:
	bumpversion patch --tag --verbose
	@echo "New version: v$$(python setup.py --version)"
	@echo "Make sure to push the new tag to GitHub"

bump-minor:
	bumpversion minor --tag --verbose
	@echo "New version: v$$(python setup.py --version)"
	@echo "Make sure to push the new tag to GitHub"

bump-major:
	bumpversion major --tag --verbose
	@echo "New version: v$$(python setup.py --version)"
	@echo "Make sure to push the new tag to GitHub"

bump-dev:
#FIXME this is currently broken
	bumpversion build --tag --verbose
	@echo "New version: v$$(python setup.py --version)"
	@echo "Make sure to push the new tag to GitHub"