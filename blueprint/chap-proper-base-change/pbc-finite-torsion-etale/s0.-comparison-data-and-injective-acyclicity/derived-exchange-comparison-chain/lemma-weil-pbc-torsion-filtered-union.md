+++
id = "lemma-weil-pbc-torsion-filtered-union"
kind = "lemma"
title = "Filtered torsion union"
order = 1640
+++
For every torsion sheaf $F$ the inclusions $F[n]\hookrightarrow F[mn]$ form a
filtered system and the canonical map $\varinjlim_nF[n]\to F$ is an
isomorphism.

## Proof

The transition map sends a section killed by $n$ to the same section, now
regarded as killed by $mn$. The map to $F$ is monic because a section that is
zero in $F$ is already zero in every $F[n]$. It is epic because every local
section of $F$ is killed by some positive integer and hence is locally in one
of the $F[n]$; sheafification preserves this local epimorphism.
