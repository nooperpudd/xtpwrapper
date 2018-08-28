clean:
	python3 setup.py clean --all
	rm -rf build dist

	find ./xtpwarpper/ -name "quote_api.so"  -delete
	find ./xtpwrapper/ -name "libxtpquoteapi.so" -delete
	find ./xtpwrapper/ -name "libxtptraderapi.so" -delete
	find ./xtpwrapper/ -name "libxtpquoteapi.dylib" -delete
	find ./xtpwrapper/ -name "libxtptraderapi.dylib" -delete

#	find ./xtpwarpper/ -name "Trader*.so"  -delete
	find ./xtpwarpper/ -name "*.cpp" -delete

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