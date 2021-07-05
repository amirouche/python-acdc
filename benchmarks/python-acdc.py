import sys
import acdc
import benchmarks as b


def init():
    science = open('data/science.txt').read().lower().encode('utf8')
    names = open('data/names.txt').read().lower().splitlines()
    loremipsum = open('data/loremipsum.txt').read().lower().encode('utf8')
    return dict(science=science, names=names, loremipsum=loremipsum)


def make(keywords):
    machine = acdc.make(keywords)
    return machine


def search(machine, data):
    out = acdc.search(machine, data)
    out = list(out)
    return out


b.science(init, make, search)
b.loremipsum(init, make, search)
