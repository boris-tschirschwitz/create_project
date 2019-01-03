SHELL := /bin/bash

.PHONY: all distclean envclean gitclean dataclean rawclean

all: env .git data data/raw

env:
	python3 -m venv env
	ln -s env/bin/activate activate

.git:
	git init
	git add .
	git commit -m "Initial commit"

data:
	mkdir data

data/raw: data
	mkdir data/raw


# Clean commands

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
	rmdir data/raw
endif
