# Experiment 007 / The morphology of possibility

Exploratory exact state-space audit. The test reconstructs the proposal rules of the prior samplers; it does not directly execute their large-network implementations.

| Family | Configurations | Constraint classes | Disconnected classes | After triangle reversals |
|---|---:|---:|---:|---:|
| 5 nodes, 5 directed edges | 15504 | 8861 | 1011 | 541 |
| 5 nodes, 6 directed edges | 38760 | 21590 | 3005 | 990 |
| 6 nodes, 6 edges, layered DAG | 924 | 731 | 0 | — |

Neural-type classes preserve labeled node in-degree, out-degree and reciprocal degree. In one 21-state class, 15 configurations contain zero induced feedforward motifs and six contain one. Uniform probability is 6/21; a simulation of 100,000 retained steps from the largest accessible component encountered none. This shows a general limitation of the proposal family, not that the actual connectome's configuration space is disconnected.

The observed neural motif count remains 3,404; the previous enrichment estimates are conditional on the sampled space. Directed triangle reversals improve reachability but do not establish irreducibility under the reciprocity constraints. The strict layered null models have a conditional connectivity argument via fixed-margin bipartite edge switches within disjoint blocks. Mixing remains unresolved.

The original computational archive is not yet hosted in this repository. These are reported experimental summaries, not an independently replicated audit.
