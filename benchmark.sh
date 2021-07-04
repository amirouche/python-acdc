#!/bin/sh

echo $(date) > benchmark.txt

echo $1 $2 >> benchmark.txt

echo $(python --version) >> benchmark.txt
python benchmark-acdc.py $1 $2 >> benchmark.txt
python benchmark-ahocorapy.py $1 $2 >> benchmark.txt

echo >> benchmark.txt
echo $(pypy3 --version) >> benchmark.txt
pypy3 benchmark-acdc.py $1 $2 >> benchmark.txt
pypy3 benchmark-ahocorapy.py $1 $2 >> benchmark.txt
