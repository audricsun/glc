.PHONY: test, testd
.SILENT:

IMAGE_NAME ?= evinoca/glc
IMAGE_TAG ?= latest

build:
	 docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

test:
	python -m py.test

testd:
	docker run -v $${pwd}:. ${IMAGE_NAME}:${IMAGE_TAG} python -m pytest

testv:
	pipenv install --dev
	make test

ptw:
	# run pytest-watch with pipenv over workspace changes
	PYTHONPATH=. pipenv run ptw

upload:
	# related packages are installed on host, not included in pipenv
	rm -rf ./dist/
	python setup.py sdist bdist_wheel
	twine upload dist/*
