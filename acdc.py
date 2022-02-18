from collections import namedtuple


IState = namedtuple(
    'IState',
    ('uid', 'parent', 'byte', 'transitions', 'longest_strict_suffix', 'match')
)


def make_state_factory():
    UID = 0
    def make_state(parent, byte):
        nonlocal UID
        uid = UID
        UID += 1
        return IState(uid, parent, byte, {}, [None], [None])
    return make_state


def make(iterable):
    make_state = make_state_factory()

    # first step: basic state machine...
    zero = make_state(None, None)
    zero.longest_strict_suffix[0] = zero

    states = [zero]
    for item in iterable:
        current = zero
        bytes = item.encode('utf8')
        for byte in bytes:
            try:
                current = current.transitions[byte]
            except KeyError:
                next = make_state(current, byte)
                states.append(next)
                current.transitions[byte] = next
                current = next
        current.match[0] = item

    # second step: finalize state machine...

    todo = set()
    todo.add(0)
    done = set()

    while todo:
        uid = todo.pop()
        state = states[uid]
        done.add(uid)

        for child in state.transitions.values():
            if child.uid not in done:
                _finalize(child, zero)
                todo.add(child.uid)

    # last step: freeze!
    out = []
    for istate in states:
        transitions = [None] * 255
        for byte, state in istate.transitions.items():
            transitions[byte] = state.uid
        fstate = FState(
            istate.byte,
            istate.match[0],
            istate.longest_strict_suffix[0].uid if istate.longest_strict_suffix[0] is not None else 0,
            tuple(transitions)
        )
        out.append(fstate)

    return tuple(out)


def _finalize(state, zero):

    parent = state.parent
    traversed = parent.longest_strict_suffix[0]

    while True:
        if state.byte in traversed.transitions.keys() and traversed.transitions[state.byte] is not state:
            state.longest_strict_suffix[0] = traversed.transitions[state.byte]
            break
        elif traversed is zero:
            state.longest_strict_suffix[0] = zero
            break
        else:
            traversed = traversed.longest_strict_suffix[0]

    suffix = state.longest_strict_suffix[0]

    if suffix is zero:
        return

    if suffix.longest_strict_suffix is None:
        _finalize(suffix)

    for byte, next in suffix.transitions.items():
        if byte not in state.transitions.keys():
            state.transitions[byte] = next


FState = namedtuple('FState', ('byte', 'match', 'longest_strict_suffix', 'transitions'))


def search(machine, iterable):
    current = zero = machine[0]
    for byte in iterable:
        index = current.transitions[byte] or zero.transitions[byte] or 0
        current = state = machine[index]
        while state is not zero:
            if state.match:
                yield state.match
            state = machine[state.longest_strict_suffix]

