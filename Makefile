clean:
	python3 setup.py clean --all
	rm -rf build dist
	find ./xtpwrapper/ -name "*.dylib" -delete
	find ./xtpwrapper/ -name "*.so" -delete
	find ./xtpwrapper/ -name "*.cpp" -delete

.PHONY: build-local
build-local: clean
	python3 setup.py build_ext --inplace

.PHONY: build
build: clean
	python3 setup.py build

.PHONY: install
install: clean
	python3 setup.py install

.PHONY: sdist
sdist: clean
	python3 setup.py sdist

twine:
	twine upload dist/*
test:
	pytest -v -s