SHELL := /bin/bash
all: env data data/raw

env:
	python3 -m venv env
	ln -s env/bin/activate activate

data:
	mkdir data

data/raw: data
	mkdir data/raw

# Clean commands

distclean: envclean dataclean

envclean:
	rm -f activate
	rm -rf env

dataclean: rawclean
ifneq (, $(wildcard data))
	rmdir data
endif

rawclean:
ifneq (, $(wildcard data/raw))
	rmdir data/raw
endif
