#!/bin/sh

export PYTHONPATH=$(pwd)

echo $(date) > benchmarks.txt

echo $1 $2 $3 >> benchmarks.txt

echo $(python --version) >> benchmarks.txt
python benchmarks/acdcb.py $1 $2 $3 >> benchmarks.txt
python benchmarks/ahocorapy.py $1 $2 $3 >> benchmarks.txt

echo >> benchmarks.txt
echo $(pypy3 --version) >> benchmarks.txt
pypy3 benchmarks/acdcb.py $1 $2 $3 >> benchmarks.txt
pypy3 benchmarks/ahocorapy.py $1 $2 $3 >> benchmarks.txt
