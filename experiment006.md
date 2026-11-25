# Experiment 006 · Sampler reliability

25 November 2026 · Edition 02 · Exploratory research

## Design

Earlier controls terminated on successful swaps. This audit includes rejected proposals in a fixed attempt budget. A fixed-accepted stopping rule can change the effective sampling distribution. Stability of a statistic is weaker than proof of sampling convergence.

### Mathlib

137,046 declarations; 304,433 dependencies. Four seeds, 61125000–61125003. Preserve exact in/out-degree and each node's counts of connections to original longest-path layer/source-directory categories; reject loops, duplicates and inadmissible swaps. Both budgets repeat the same seeded prefix. Observed 27,244 motifs. Degrees and levels checked at endpoints.

| Seed offset | 5 attempts/edge | 25 attempts/edge | Original-edge overlap (25) |
|---:|---:|---:|---:|
|0|5060|5033|0.124921|
|1|5020|4926|0.125226|
|2|4958|4959|0.125190|
|3|4897|4997|0.124796|

Medians 4,989 and 4,978. The longer-run enrichment is 5.47288×. Each longer chain attempts 7,610,825 swaps. Accepted counts: 6,599,059; 6,598,357; 6,600,616; 6,597,752. Only four chains and two checkpoints; no R-hat, ESS or irreducibility claim.

### Neural chemical connectome

453 vertices; 4,841 distinct non-loop directed edges. Preserve in/out-degree and reciprocal degree at every node. Unidirectional and reciprocal dyads are selected proportional to their counts; reject loops, duplicates or changes to reciprocity. Eight seeded chains, four empirical starts and four pre-randomized for 20 attempts per edge. Each chain then runs 40 attempts per edge, recording each edge-count of attempted proposals; first ten checkpoints omitted for diagnostic summary. Observed 3,404 induced 030T feedforward motifs; pooled late median 1,553 (range 1,436–1,681); ratio 2.19189. Empirical-start median 1,555; pre-randomized-start median 1,552. Rank-normalized split R-hat 1.030615; folded 0.990132. The larger value does not meet the stringent 1.01 target. Lag-one sample correlations range −0.167 to 0.216. Final control median 1,534.5; endpoint values by chain: 1629,1582,1516,1521,1549,1453,1548,1499. Final original-edge overlap median 0.078599. The 240 late measurements are correlated; pre-randomized starts remain within the same sampler family.

### E. coli

423 nodes; 519 non-loop directed edges. Sixteen seeded, hierarchy- and degree-preserving trajectories from the observed graph. Fixed-attempt checkpoint at 100 attempts per edge: median 12, range 8–20; observed 42. The result persists under a changed stopping procedure, but global mixing remains unresolved.

## Next validation

Longer Mathlib traces with diverse starts, additional independent proposal implementations, effective sample sizes for relevant statistics, tests of reachable state spaces on exactly enumerable small graphs, and checks for sensitivity to graph definitions. No uniform-sampling guarantee or formal statistical significance is asserted.
