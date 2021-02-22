from queue import Queue

src = [1, 2, 3, 4, 5, 6, 7, 8,-1]
target = [-1, 2, 3, 4, 5, 8, 1, 6, 7]

def h(state):
    res = 0
    for i in range(1, 9):
        if state.index(i) != target.index(i): res += 1
    return res

def gen(state, m, b):
    temp = state[:]
    if m == 'l': temp[b], temp[b - 1] = temp[b - 1], temp[b]
    if m == 'r': temp[b], temp[b + 1] = temp[b + 1], temp[b]
    if m == 'u': temp[b], temp[b - 3] = temp[b - 3], temp[b]
    if m == 'd': temp[b], temp[b + 3] = temp[b + 3], temp[b]
    return temp

def movimientosPosibles(state, visited_states):
    b = state.index(-1)
    d = []
    pos_moves = []
    if b <= 5: d.append('d')
    if b >= 3: d.append('u')
    if b % 3 > 0: d.append('l')
    if b % 3 < 2: d.append('r')
    for i in d:
        temp = gen(state, i, b)
        if not temp in visited_states: pos_moves.append(temp)
    return pos_moves

def buscar(src, target, visited_states, g):
    if src == target: return visited_states
    visited_states.append(src),
    adj = movimientosPosibles(src, visited_states)
    scores = []
    selected_moves = []
    for move in adj: scores.append(h(move) + g)
    if len(scores) == 0:
        min_score = 0
    else:
        min_score = min(scores)
    for i in range(len(adj)):
        if scores[i] == min_score: selected_moves.append(adj[i])
    for move in selected_moves:
        if buscar(move, target, visited_states, g + 1): return visited_states
    return None

def bfs_buscar(src, target, visited_states):
    q = Queue()
    q.put((src, 0))
    while not q.empty():
        curr, g = q.get()
        if target == curr: return visited_states
        visited_states.append(curr)
        adj = movimientosPosibles(curr, visited_states)
        scores = []
        selected_moves = []
        for move in adj: scores.append(h(move) + g)
        if len(scores) == 0:
            min_score = 0
        else:
            min_score = min(scores)
        for i in range(len(adj)):
            if scores[i] == min_score: selected_moves.append(adj[i])
        for move in selected_moves: q.put((move, g + 1))
    return None

def solve(src, target, bfs=True):
    visited_states = []
    if bfs:
        res = bfs_buscar(src, target, visited_states)
    else:
        res = buscar(src, target, visited_states, 0)
    if res:
        i = 0
        for state in res:
            print('move :', i + 1, end="\n")
            print()
            display(state)
            i += 1
        print('move :', i + 1)
        display(target)

def display(state):
    print()
    for i in range(9):
        if i % 3 == 0: print()
        if state[i] == -1:
            print(state[i], end="\t")
        else:
            print(state[i], end="\t")
    print(end="\n")

def run():
    print('Estado inicial :')
    display(src)
    print('Estado final :')
    display(target)
    print('*' * 10)
    solve(src, target)

