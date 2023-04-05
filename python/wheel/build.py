# python setup.py sdist bdist_wheel >> build pure-python/universal wheel + source distrib

# python setup.py bdist_wheel --universal >> specifies universal (py2+py3) wheel build for pure python project

# platform wheel (C extensioin somewhere)
# platform wheel with manylinux docker images
# for those one can bundle shared libraries (.so) with autditwheel/delocate > will package the .so as a .dylib

# then use twine/poetry to publish your wheel