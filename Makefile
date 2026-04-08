APP = $(shell basename $$(pwd))

all: format test clean

push: convert-conf slim-deploy
	python -m mpremote cp -r sources/encoded/* :/apps/${APP}/sources/encoded/
	python -m mpremote cp -r common :/apps/${APP}/
	python -m mpremote cp -r conf.json :/apps/${APP}/
	python -m mpremote cp -r metadata.json :/apps/${APP}/
	python -m mpremote cp -r tildagon.toml :/apps/${APP}/

slim-deploy:
	python -m mpremote cp -r lib :/apps/${APP}/
	python -m mpremote cp app.py :/apps/${APP}/

mkdir:
	-python -m mpremote mkdir apps/${APP}
	-python -m mpremote mkdir apps/${APP}/sources
	-python -m mpremote mkdir apps/${APP}/sources/encoded

connect:
	python -m mpremote

deploy: mkdir push connect

convert-conf:
	@python scripts/conf_yaml_to_json.py

format:
	ruff format
	ruff check --fix

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .ruff_cache -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;
	@find . -depth -name .DS_Store -exec rm -fr {} \;

test: convert-conf
	python -m pytest \
		--random-order \
		--verbose \
		--capture no \
		--exitfirst \
		--last-failed

generate:
	python tools/splitter.py
	python tools/bitmapper.py
	python tools/slimmer.py
	python tools/encoder.py

clean-sources:
	rm -fr sources/bitmaps/
	rm -fr sources/crops/
	rm -fr sources/encoded/
	rm -fr sources/slimmed_bitmaps/

install: guard-LIBRARY
	mkdir -p pikesley
	rsync --archive --verbose --exclude tests ../pikesley/${LIBRARY} pikesley/

build:
	docker build \
		--build-arg APP=${APP} \
		--tag ${APP} .

run:
	docker run \
		--name ${APP} \
		--hostname ${APP} \
		--volume $(shell pwd):/opt/${APP} \
		--interactive \
		--tty \
		--rm \
		${APP} \
		bash

guard-%:
	@if [ -z "${${*}}" ] ; \
    then \
        echo "You must provide the ${*} variable" ; \
        exit 1 ; \
    fi

-include Makefile.local
