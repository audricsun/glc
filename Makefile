.PHONY: test, testd
.SILENT:

IMAGE_NAME ?= evinoca/gli
IMAGE_TAG ?= latest

build:
	 docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

test:
	python -m py.test \
		--junit-xml=reports.xml \
		--cov-report term-missing \
		--cov-report xml:coverage.xml \
		--cov=gli

testd:
	docker run -v $${pwd}:. ${IMAGE_NAME}:${IMAGE_TAG} python -m pytest

testv:
	pipenv install --dev
	make test
