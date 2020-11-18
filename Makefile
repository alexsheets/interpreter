MODULES = Parse Print Special Tokens Tree Scheme4101.py Util.py
FILES = SPP.py Makefile fac.scm

all:
	python3 -m compileall ${MODULES}

clean:
	rm -f *~ */*~

veryclean:
	rm -f *~ */*~
	rm -rf __pycache__ */__pycache__
