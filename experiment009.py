#!/usr/bin/env python3
"""Exact enumeration, independent of the visualizer's transition table."""
import itertools, json, csv
from collections import Counter
from pathlib import Path
N=5
E=list(itertools.permutations(range(N),2))
def degree(g):
    return tuple((sum(a==i for a,b in g),sum(b==i for a,b in g),sum(a==i and (b,a) in g for a,b in g)) for i in range(N))
target=((2,1,0),(1,1,0),(1,2,0),(1,1,0),(1,1,0))
states=[frozenset(g) for g in itertools.combinations(E,6) if degree(frozenset(g))==target]
published=[[[0,1],[0,3],[1,2],[2,0],[3,4],[4,2]],[[0,1],[0,3],[1,4],[2,0],[3,2],[4,2]],[[0,1],[0,4],[1,2],[2,0],[3,2],[4,3]],[[0,1],[0,4],[1,3],[2,0],[3,2],[4,2]],[[0,3],[0,4],[1,2],[2,0],[3,1],[4,2]],[[0,3],[0,4],[1,2],[2,0],[3,2],[4,1]],[[0,1],[0,2],[1,3],[2,4],[3,2],[4,0]],[[0,1],[0,3],[1,2],[2,4],[3,2],[4,0]],[[0,2],[0,3],[1,2],[2,4],[3,1],[4,0]],[[0,1],[0,2],[1,4],[2,3],[3,0],[4,2]],[[0,1],[0,4],[1,2],[2,3],[3,0],[4,2]],[[0,2],[0,4],[1,2],[2,3],[3,0],[4,1]],[[0,2],[0,3],[1,0],[2,1],[3,4],[4,2]],[[0,2],[0,4],[1,0],[2,1],[3,2],[4,3]],[[0,3],[0,4],[1,0],[2,1],[3,2],[4,2]],[[0,1],[0,2],[1,2],[2,3],[3,4],[4,0]],[[0,1],[0,2],[1,2],[2,4],[3,0],[4,3]],[[0,2],[0,3],[1,0],[2,4],[3,2],[4,1]],[[0,2],[0,3],[1,4],[2,1],[3,2],[4,0]],[[0,2],[0,4],[1,0],[2,3],[3,1],[4,2]],[[0,2],[0,4],[1,3],[2,1],[3,0],[4,2]]]
G=[frozenset(map(tuple,g)) for g in published]
assert len(states)==len(G)==len(set(G))==21 and set(states)==set(G)
def motif(g):
    return sum((a,b) in g and (b,c) in g and (a,c) in g and not any(x in g for x in [(b,a),(c,b),(c,a)]) for a,b,c in itertools.permutations(range(N),3))
def relabel(g,p):
    return frozenset((p[a],p[b]) for a,b in g)
P=[(0,b,2,d,e) for b,d,e in itertools.permutations([1,3,4])]
orbits=[]
remaining=set(range(len(G)))
while remaining:
    i=min(remaining)
    o=sorted({G.index(relabel(G[i],p)) for p in P})
    orbits.append(o); remaining.difference_update(o)
def move(g,h,mode):
    k=len(g-h)
    if mode==0:return k==2
    if mode==1:return k==2 or (k==3 and frozenset((b,a) for a,b in g-h)==h-g and len(set(a for a,b in g-h))==3 and set(a for a,b in g-h)==set(b for a,b in g-h))
    return 1<=k<=3
A=[[[j for j,h in enumerate(G) if move(g,h,m)] for g in G] for m in range(3)]
def component(adj,i):
    seen={i}; q=[i]
    for a in q:
        for b in adj[a]:
            if b not in seen:seen.add(b);q.append(b)
    return seen
Q=[]
for adj in A:
    matrix=[]
    for o in orbits:
        rows=[[sum(j in p for j in adj[i]) for p in orbits] for i in o]
        assert all(r==rows[0] for r in rows)
        matrix.append(rows[0])
    Q.append(matrix)
print("Orbits:",[[i+1 for i in o] for o in orbits])
print("Reach:",[len(component(a,0)) for a in A])
print("Motifs:",[motif(g) for g in G])
print("Quotient matrices:",Q)
with open("experiment009_states.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(["state","orbit","motifs","switch_neighbors","triangle_enabled_neighbors","three_edge_neighbors"])
    for i,g in enumerate(G):w.writerow([i+1,next(k+1 for k,o in enumerate(orbits) if i in o),motif(g),*[len(a[i]) for a in A]])
