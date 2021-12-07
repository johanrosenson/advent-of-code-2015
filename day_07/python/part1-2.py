import re

signals = open('../input.txt').read().splitlines()

wires = {}

def resolve_signals(signals, override_wire = None, override_op = None):
    remaining = []

    for signal in signals:
        [op, wire] = re.match(r'(.+?)\s+->\s+(.+)', signal).groups()
        if wire == override_wire and override_op != None:
            op = override_op
        value = resolve_op(op)
        if value != None:
            wires[wire] = value
        else:
            remaining.append(signal)

    if len(remaining) > 0:
        resolve_signals(remaining, override_wire, override_op)

def resolve_op(op):
    match = re.match(r'(\S+)\s+(AND|OR|[LR]SHIFT)\s+(\S+)', op)
    if match != None:
        [a, gate, b] = match.groups()
        if gate == 'AND':
            return and_gate(a, b)
        if gate == 'OR':
            return or_gate(a, b)
        if gate == 'LSHIFT':
            return lshift(a, b)
        if gate == 'RSHIFT':
            return rshift(a, b)

    match = re.match(r'NOT\s+(\S+)', op)
    if match != None:
        return not_gate(match.group(1))

    return resolve_wire(op)

def resolve_wire(w):
    if w.isnumeric():
        return int(w)

    return wires.get(w)

def and_gate(a, b):
    [x, y] = [resolve_wire(a), resolve_wire(b)]
    if x == None or y == None:
        return None

    return x & y

def or_gate(a, b):
    [x, y] = [resolve_wire(a), resolve_wire(b)]
    if x == None or y == None:
        return None

    return x | y

def lshift(a, b):
    [x, y] = [resolve_wire(a), resolve_wire(b)]
    if x == None or y == None:
        return None

    return x << y

def rshift(a, b):
    [x, y] = [resolve_wire(a), resolve_wire(b)]
    if x == None or y == None:
        return None

    return x >> y

def not_gate(a):
    x = resolve_wire(a)
    if x == None:
        return None

    return ~ x & 0xffff # convert to 16-bit number

resolve_signals(signals)
print('a: {}'.format(wires['a']))

override_op = wires['a']
wires = {}

resolve_signals(signals, 'b', str(override_op))
print('a: {}'.format(wires['a']))
