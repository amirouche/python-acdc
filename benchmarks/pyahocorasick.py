import ahocorasick
import benchmarks as b


def init():
    science = open('data/science.txt').read().lower()
    names = open('data/names.txt').read().lower().splitlines()
    loremipsum = open('data/loremipsum.txt').read().lower()
    return dict(science=science, names=names, loremipsum=loremipsum)


def make(keywords):
    A = ahocorasick.Automaton()
    for keyword in keywords:
        A.add_word(keyword, keyword)
    A.make_automaton()
    return A


def search(machine, data):
    out = list()
    for _, keyword in machine.iter(data):
        out.append(keyword)
    return out


b.science(init, make, search)
b.loremipsum(init, make, search)
