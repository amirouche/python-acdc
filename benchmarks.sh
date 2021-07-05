#!/bin/sh

export PYTHONPATH=$(pwd)

rm *.benchmarks.txt

echo $(python --version)
python benchmarks/python-acdc.py $1 $2 $3
python benchmarks/ahocorapy.py $1 $2 $3
python benchmarks/pyahocorasick.py $1 $2 $3

echo $(pypy3 --version)
pypy3 benchmarks/python-acdc.py $1 $2 $3
pypy3 benchmarks/ahocorapy.py $1 $2 $3
pypy3 benchmarks/pyahocorasick.py $1 $2 $3
