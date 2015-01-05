default:
	cd demo && make

deploy_test:
	python setup.py register -r test
	python setup.py sdist upload -r test
	#pip install -i https://testpypi.python.org/pypi <package name>

deploy_production:
	# git switch to master and push
	python setup.py sdist
	python setup.py register -r pypi
	twine upload dist/*

