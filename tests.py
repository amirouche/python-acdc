import acdc



def test_empty_keyword():
    machine = acdc.make([])
    assert len(list(acdc.search(machine, "abcdefijklmnopqrstuvwxyz".encode('utf8')))) == 0

def test_empty_search():
    machine = acdc.make(["abc"])
    assert len(list(acdc.search(machine, ""))) == 0

def test_nominal():
    machine = acdc.make(["abc", "xyz", "mno"])
    assert list(acdc.search(machine, "abcdefijklmnopqrstuvwxyz".encode('utf8')
    )) == ["abc", "mno", "xyz"]

def test_suffixes():
    machine = acdc.make(["abc", "bc", "c"])
    assert list(acdc.search(machine, "abcdefijklmnopqrstuvwxyz".encode('utf8'))) == ["abc", "bc", "c"]


if __name__ == '__main__':
    unittest.main()
