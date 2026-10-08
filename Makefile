SIZE ?= 1000
ARGS ?=

all: lsystem.png

lsystem.png: lsystem.pov
	povray +W$(SIZE) +H$(SIZE) +A0.3 -D -GA +I$< +O$@

lsystem.pov: romanesco-lsystem.py
	python3 romanesco-lsystem.py $(ARGS) > $@

clean:
	rm -f lsystem.pov lsystem.png

.PHONY: all clean
