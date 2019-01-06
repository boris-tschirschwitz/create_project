SHELL := /bin/bash

.PHONY: all

all: env/.requirements.lastrun .git | env data data/raw

env:
	python3 -m venv env
	ln -s env/bin/activate activate

env/.requirements.lastrun: requirements.txt | env
	source activate && pip install -r requirements.txt
	touch env/.requirements.lastrun

.git:
	git init
	git add .
	git commit -m "Initial commit"

data:
	mkdir data

data/raw: | data
	mkdir data/raw


# Clean commands

.PHONY: distclean envclean gitclean dataclean rawclean

distclean: envclean gitclean dataclean

envclean:
	rm -f activate
	rm -rf env

gitclean:
	rm -rf .git

dataclean: rawclean
ifneq (, $(wildcard data))
	rmdir data
endif

rawclean:
ifneq (, $(wildcard data/raw))
	rm -rf data/raw
endif
